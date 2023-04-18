import pymongo
import json


from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List
from bson import ObjectId, json_util
from datetime import datetime, timedelta

router = APIRouter(prefix="/api")

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Eshop"]
collection = db["merchs"]


class Product(BaseModel):
    searchKeyword: str = ""
    sort_by: str = "price_desc"
    create_at:datetime = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

@router.post ("/products")
async def search_products(data : Product):

    search_params = {}
    sort_params = {}

    if data.searchKeyword:
        search_params["searchKeyword"] = {"$regex": data.searchKeyword, "$options": "i"}

    if data.sort_by == "price_desc": 
        sort_params["price"] = pymongo.DESCENDING
    elif data.sort_by == "price_asc":  
        sort_params["price"] = pymongo.ASCENDING

    if search_params:
        result = collection.find(search_params).sort(list(sort_params.items()))
        count = collection.count_documents(search_params)
        result = json.loads(json_util.dumps(result)) 
    return {"count": count, "products": list(result)}