import asyncio
import httpx
import random
from datetime import datetime


async def send_request(session, thread_num, request_num, delay):
    sleep_time = random.uniform(*delay)

    request = {"id": request_num, "delay": sleep_time}

    response = await session.post("http://localhost:8001/recieve/", json=request)

    # logger
    print(f"Time: {datetime.now()}, Thread: {thread_num}, Request: {request}, Response: {response.status_code}")


async def main(connection_count, connection_value, delay_range):
    requests_per_connection = connection_value // connection_count

    async with httpx.AsyncClient() as session:
        tasks = []
        for thread_num in range(connection_count):
            for request_num in range(requests_per_connection):
                task = send_request(session, thread_num, request_num, delay_range)
                tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == "__main__":
    connection_count = 5
    connection_value = 100
    delay_range = (1, 5)

    asyncio.run(main(connection_count, connection_value, delay_range))
