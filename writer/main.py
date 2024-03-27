from fastapi import FastAPI, Request
import datetime
import asyncio
import os


app = FastAPI()

write_lock = asyncio.Lock()


async def write_to_file(file_name, content):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, file_name)

    async with write_lock:
        with open(full_path, "a") as file:
            file.write(content + "\n")


@app.post("/write_recieve/")
async def write_recieve(request: Request):
    request_data = await request.json()
    print(f"Received in writer: {request_data}")
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
