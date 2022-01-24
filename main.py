from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return {"data":True}


# route API 
# app.include_router(sensor)

# @app.post("/Sensors", response_description="Add new sensor data", response_model=SensorSavingModel)
# async def create_data(senData: SensorEntryModel):
    
#     doc = dict((k, v) for k, v in senData.dict().items() if v is not None)
#     doc['updatedAt'] = getUpdateTime()
#     doc['timestamp'] = now()
    
#     # fdoc = SensorSavingModel.parse_obj()
        
#     if res := conn.Sensor.insert_one(doc):
#         return SensorSavingModel.parse_obj(conn.Sensor.find_one({'_id':ObjectId(res.inserted_id)})) 
#     else:
#         return False