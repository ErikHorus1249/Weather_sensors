from fastapi import APIRouter
# from dat.Models import SensorEntryModel, SensorSavingModel
from database.Models import *
from database.Connect import conn
from bson.objectid import ObjectId
from features import *
from features.DateTime import getNow, getUpdateTime, now

sensor = APIRouter()

@sensor.get("/", response_description="Root directory!")
async def get_root():
    
    return {"data":True}

@sensor.post("/Sensor/create", response_description="Add new sensor data", response_model=SensorSavingModel)
async def create_data(senData: SensorEntryModel):
    
    doc = dict((k, v) for k, v in senData.dict().items() if v is not None)
    doc['updatedAt'] = getUpdateTime()
    doc['timestamp'] = now()
    
    # fdoc = SensorSavingModel.parse_obj()
        
    if res := conn.Sensor.insert_one(doc):
        return SensorSavingModel.parse_obj(conn.Sensor.find_one({'_id':ObjectId(res.inserted_id)})) 
    else:
        return False