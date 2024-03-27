from fastapi import FastAPI, Request
import datetime
import asyncio


app = FastAPI()

write_lock = asyncio.Lock()


async def write_to_file(file_name, content):
    async with write_lock:
        with open(file_name, "w+") as file:
            file.write(content + "\n")


@app.post("/write_recieve/")
async def write_recieve(request: Request):
    request_data = await request.json()
    recieve_time = request_data.get('recieve_time', 'Not Provided')
    await write_to_file("recieved_requests.txt", f"{request_data['id']} | {recieve_time}")
    return {"status": "Processed"}


@app.post("/write_after_delay/")
async def write_after_delay(request: Request):
    request_data = await request.json()
    recieve_time = request_data.get('recieve_time', 'Not Provided')
    write_time = datetime.datetime.now()

    await write_to_file("processed_requests.txt", f"{request_data['id']} | {recieve_time} | {write_time}")
    return {"status": "Processed"}
