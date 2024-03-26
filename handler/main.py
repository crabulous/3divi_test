from fastapi import FastAPI, requests
import datetime
import asyncio
from pydantic import BaseModel
import time


class RequestModel(BaseModel):
    id: int
    delay: int
    recieve_time: str


app = FastAPI()


@app.post("/handler/")
async def handler_request(request: RequestModel):
    await requests.post("http://localhost:8004/write_recieve/", json=request)
    await asyncio.sleep(request.delay)
    await requests.post("http://localhost:8004/write_after_delay/", json=request)

    return {"handler": "Ok"}
