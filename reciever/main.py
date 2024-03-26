from fastapi import FastAPI, requests
import datetime
from pydantic import BaseModel


class RequestModel(BaseModel):
    id: int
    delay: int


app = FastAPI()


@app.post("/recieve/")
async def recieve_request(request: RequestModel):
    recieve_time = datetime.datetime.now()
    request.recieve_time = recieve_time
    await requests.post("http://localhost:8002/handler/", json=request)
    print(f"Request recieved at: {recieve_time}. Request ID: {request.id}")
    return {"asyncAnswer": "Ok"}
