from fastapi import FastAPI
from routes.Sensor import sensor

app = FastAPI()

# @app.get("/")
# def get_root():
#     return {"data":True}


# route API 
app.include_router(sensor)