import time

from fastapi import FastAPI, requests
import datetime
import asyncio
from pydantic import BaseModel


class RequestModel(BaseModel):
    id: int
    delay: int
    recieve_time: str


app = FastAPI()


async def write_to_file(file_name, content):
    async with asyncio.Lock():
        with open(file_name, "a") as file:
            file.write(content + "\n")


@app.post("/write_recieve/")
async def write_recieve(request: RequestModel):

    await write_to_file("recieved_requests.txt", f"{request.id} | {request.recieve_time}")

    return {"status": "Processed"}


@app.post("/write_after_delay/")
async def write_after_delay(request: RequestModel):
    write_time = datetime.datetime.now()

    await write_to_file("processed_requests.txt", f"{request.id} | {request.recieve_time} | {write_time}")

    return {"status": "Processed"}
