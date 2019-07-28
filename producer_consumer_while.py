import time
from datetime import datetime


def consumer():
    temp_task = None
    while True:
        temp_task = yield f'{temp_task}完成，time:{datetime.now()}'
        print(f'\n处理{temp_task}，time:{datetime.now()}')
        time.sleep(1)
        print(f'完成{temp_task}，time:{datetime.now()}')


task_handler = consumer()
task_handler.send(None)
n = 1



while True:
    task = f'{n}号任务'
    print(f'发送{task}，time:{datetime.now()}')
    print(task_handler.send(task))
    n += 1

