from fastapi import FastAPI, Request
import asyncio
from pydantic import BaseModel
import httpx


# class RequestModel(BaseModel):
#     id: int
#     delay: int
#     recieve_time: str


app = FastAPI()


@app.post("/handler/")
async def handler_request(request: Request):
    request_data = await request.json()
    #print("REQUEST DATADATADATA", request_data)
    async with httpx.AsyncClient() as client:
        await client.post("http://writer:8000/write_recieve/", json=request_data)
    await asyncio.sleep(request_data['delay'])
    async with httpx.AsyncClient() as client:
        await client.post("http://writer:8000/write_after_delay/", json=request_data)

    return {"handler": "Ok"}
