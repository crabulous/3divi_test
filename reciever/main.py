from fastapi import FastAPI, Request
import datetime
import httpx


app = FastAPI()


@app.post("/recieve/")
async def recieve_request(request: Request):
    recieve_time = datetime.datetime.now().isoformat()
    request_data = await request.json()
    request_data['recieve_time'] = recieve_time

    async with httpx.AsyncClient() as client:
        await client.post("http://handler:8000/handler/", json=request_data)

    return {"asyncAnswer": "Ok"}
