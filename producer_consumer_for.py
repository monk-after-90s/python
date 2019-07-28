import time
from datetime import datetime


def consumer():
    temp_task = None
    while True:
        temp_task = yield f'{temp_task}完成，time:{datetime.now()}'
        # print(f'\n处理{temp_task}，time:{datetime.now()}')
        time.sleep(1)
        # print(f'完成{temp_task}，time:{datetime.now()}')


task_handler = consumer()
task_handler.send(None)
n = 1

for handle_result in task_handler:
    print(task_handler.send(f'{n}号任务'))
    n += 1

# for相当于不断的调用next()，上面的实现send()相当于同时调用next()和send()
#for无法很好的与生成器双向交互
