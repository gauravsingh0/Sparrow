#Kiitu
import asyncio
import sys

from motor import motor_asyncio
from YoneRobot import MONGO_DB_URI 
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from YoneRobot.conf import get_int_key, get_str_key



MONGO_DB_URI = get_str_key("MONGO_DB_URI")

client = MongoClient()
client = MongoClient(MONGO_DB_URI)
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI)
db = client["yonerobot"]
db = motor[MONGO_DB_URI]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("Can't connect to mongodb! Exiting..."))