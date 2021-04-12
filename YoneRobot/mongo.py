#Kiitu
import asyncio
import sys

from YoneRobot import MONGO_DB_URI 
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


MONGO_DB_URI = get_str_key("MONGO_DB_URI")

client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["yonerobot"]