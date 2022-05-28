import boto3
from fastapi import HTTPException
from src.settings import settings
from botocore.exceptions import ClientError

class UserDataAccess():
    def __init__(self) -> None:
        self.client = boto3.client("cognito-idp", region_name="eu-west-2")
        

    def create_user_pool(self, pool_name: str, pool_description: str) -> dict:
        response = self.client.create_user_pool(PoolName=pool_name,
                                                PoolDescription=pool_description)
        return response

    def get_user_pools(self, max_results: int = 10) -> dict:
        response = self.client.list_user_pools(MaxResults=max_results)
        return response
        
        
    def sign_up(self, user_name: str, password: str, email: str) -> dict:
        response = self.client.sign_up(ClientId=settings.client_id, Username=user_name, Password=password, UserAttributes=[
            {"Name": "email", "Value": email}
        ])
        return response

    def verify_user(self, username: str, confirmation_code: str):
        response = self.client.confirm_sign_up(ClientId=settings.client_id, Username=username, ConfirmationCode=confirmation_code)
        return response

    def sign_in(self, email: str, password: str):
        try:
            response = self.client.initiate_auth(ClientId=settings.client_id, AuthFlow="USER_PASSWORD_AUTH", AuthParameters={
                    "USERNAME": email,
                    "PASSWORD": password
                })
        except ClientError:
            raise HTTPException(
                status_code=406,
                detail="Username or password is incorrect, OR account email not verified",
            )
        access_token = response["AuthenticationResult"]["AccessToken"]
        client = boto3.client("cognito-idp", region_name="eu-west-2")
        user = client.get_user(AccessToken=access_token)
        return user, {"accessToken": access_token}

    def forgot_password(self, email: str):
        response = self.client.forgot_password(ClientId=settings.client_id, Username=email)
        return response

    def confirm_forgot_password(self, username: str, confirmation_code: str, new_password: str):
        response = self.client.confirm_forgot_password(ClientId=settings.client_id, Username=username, ConfirmationCode=confirmation_code, Password=new_password)
        return response