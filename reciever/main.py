from fastapi import FastAPI, Request
import datetime
from pydantic import BaseModel
import httpx


# class RequestModel(BaseModel):
#     id: int
#     delay: int


app = FastAPI()


@app.post("/recieve/")
async def recieve_request(request: Request):
    recieve_time = datetime.datetime.now().isoformat()
    request_data = await request.json()
    request_data['recieve_time'] = recieve_time

    async with httpx.AsyncClient() as client:
        await client.post("http://handler:8000/handler/", json=request_data)

    #print(f"Sending to handler: {request_data}")
    print(f"Request received at: {recieve_time}. Request ID: {request_data['id']}")
    return {"asyncAnswer": "Ok"}
