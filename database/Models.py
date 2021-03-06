from ast import Dict
from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel, Field
import uuid
import datetime


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class AccelerometerModel(BaseModel):
    accelerometerX: float
    accelerometerY: float
    accelerometerZ: float

class GyroscopeModel(BaseModel):
    gyroscopeX: float
    gyroscopeY: float
    gyroscopeZ: float

class TempvsHumiModel(BaseModel):
    temp: float
    humi: float
    mois: float
    
class SensorEntryModel(BaseModel):
    accelerometer: AccelerometerModel
    gyroscope: GyroscopeModel
    tempvshumi: TempvsHumiModel
    rain: float
    
class SensorSavingModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    accelerometer: AccelerometerModel
    gyroscope: GyroscopeModel
    tempvshumi: TempvsHumiModel
    rain: float
    updatedAt: str
    timestamp: float
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
    

