'''
异步发送不一样时间间隔任务的生产消费者模型
'''
import asyncio
import datetime
import time


def consumer():
    while True:
        task = yield
        print(f'处理{task}')


task_handler = consumer()
task_handler.send(None)


async def async_sleep(sleep_time: int):
    while True:
        current_time = time.time()
        print(f'发送{sleep_time}s 任务,时间:{datetime.datetime.now()}')
        task_handler.send(f'{sleep_time}s 任务')
        real_sleep_time = sleep_time - (time.time() - current_time)
        if real_sleep_time <= 0:
            continue
        else:
            await asyncio.sleep(sleep_time)


asyncio.run(asyncio.wait([async_sleep(1), async_sleep(2)]))
