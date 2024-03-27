import asyncio
import time
import httpx
import random
from datetime import datetime


async def send_request(session, thread_num, request_num, delay):
    sleep_time = random.uniform(*delay)

    request = {"id": request_num, "delay": sleep_time}

    response = await session.post("http://reciever:8000/recieve/", json=request)

    # logger
    print(f"Time: {datetime.now()}, Thread: {thread_num}, Request: {request}, Response: {response.status_code}")

    return response


async def main(connection_count, connection_value, delay_range):
    requests_per_connection = connection_value // connection_count

    async with httpx.AsyncClient(timeout=10.0) as session:
        tasks = []
        for thread_num in range(connection_count):
            for request_num in range(requests_per_connection):
                task = send_request(session, thread_num, request_num, delay_range)
                tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == "__main__":
    connection_count = 2
    connection_value = 30
    delay_range = (1, 3)
    time.sleep(2)
    asyncio.run(main(connection_count, connection_value, delay_range))
