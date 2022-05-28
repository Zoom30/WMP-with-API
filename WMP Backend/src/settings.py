from pydantic import BaseSettings

class CommonSettings(BaseSettings):
    client_id: str
    user_pool_id: str
    client_secret: str=None


settings = CommonSettings()