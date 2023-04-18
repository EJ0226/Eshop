import pymongo
import json


from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List
from bson import ObjectId, json_util

router = APIRouter()

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["fhsh_shop"]
collection = db["items"]


class Product(BaseModel):
    searchKeyword : str = ""

@router.post ("/products")
async def search_products(data : Product):
    search_params = {}
    if data.searchKeyword :
        search_params["searchKeyword "] = {"$regex": data.searchKeyword , "$options": "i"}
    if search_params:
        result = collection.find(search_params)
        result = json.loads(json_util.dumps(result)) 
    return {"products": list(result)}