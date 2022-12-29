import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorDatabase

from app import config

settings: config.Settings = config.get_settings

DB_URL = settings.api_db_url
DB_NAME = settings.api_db_name

client = motor.motor_asyncio.AsyncIOMotorClient(DB_URL)

db: AsyncIOMotorDatabase = client[DB_NAME]

