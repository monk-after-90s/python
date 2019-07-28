'''
独立协程拥有独立异步生成器
'''
import asyncio
import time
from datetime import datetime


async def async_sleep(sleep_sec: int):
    while True:
        time_mark = time.time()
        yield f'Task:{sleep_sec}s'
        await asyncio.sleep(sleep_sec - (time.time() - time_mark))


async def coro(sleep_sec: int):
    async for task in async_sleep(sleep_sec):
        print(f'Handle {task}，time:{datetime.now()}')


asyncio.run(asyncio.wait([coro(1), coro(2), coro(3)]))
