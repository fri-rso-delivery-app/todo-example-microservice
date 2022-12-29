from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    api_root_path: str = ''
    api_http_port: int = 8888
    api_db_url: str = 'mongodb://root:example@localhost:27017/'
    api_db_name: str = 'todo_service'

    # auth settings
    api_login_url: str = 'http://localhost:8001/jwt/token'
    # to get a viable secret run:
    # openssl rand -hex 32
    api_secret_key: str = 'SECRET_REPLACE_ME'
    api_jwt_algorithm: str = 'HS256'


@lru_cache()
def get_settings() -> Settings:
    return Settings()
