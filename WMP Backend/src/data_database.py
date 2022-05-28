
from uuid import uuid4
import boto3
class DBDataAccess():
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb', region_name="eu-west-2")
        self.table_name = "InitialDetailsTable"
        self.table = self.dynamodb.Table(self.table_name)
        self.initial_weight = None
        self.initial_height = None

    def set_initial_details(self, weight, height):
        self.initial_weight = weight
        self.initial_height = height
        response = self.table.put_item(Item={
            "InitialID": uuid4().hex,
            "Initial Weight": weight,
            "Initial Height": height
        })
        return response

    def get_initial_details(self):
        response = self.table.scan()
        return response

    def remove_initial_details(self, primary_key):
        response = self.table.delete_item(Key={
            "InitialID": primary_key
        })
        return response

    def remove_all_initial_details(self):
        response = self.table.scan()
        for item in response['Items']:
            print(item)
            self.table.delete_item(Key={
                "InitialID": item['InitialID']
            })
        return response

    def update_initial_detail(self, primary_key, weight, height):
        response = self.table.update_item(Key={
            "InitialID": primary_key
        }, UpdateExpression="set Initial Weight = :weight, Initial Height = :height",
            ExpressionAttributeValues={
                ':weight': weight,
                ':height': height
            })
        return response

    def set_target_weight(self, target_weight):
        
        ...

    
    def _create_table(self, table_name: str, columns: list = None):
        response = self.dynamodb.create_table(
            TableName=table_name, 
            AttributeDefinitions=[
            {
                "AttributeName": columns[0],
                "AttributeType": "S"
            }
        ], KeySchema=[
            {
                "AttributeName": columns[0],
                "KeyType": "HASH"
            }
        ], ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
            },)
        return response