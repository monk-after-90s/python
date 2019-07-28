from datetime import datetime


def consumer():
    temp_task = None
    while True:
        temp_task = yield f'{temp_task}完成，time:{datetime.now()}'
        print(f'处理{temp_task}')


task_handler = consumer()
task_handler.send(None)
# next(task_handler)
n = 1
while True:
    print(f'task_handler:{next(task_handler)}')
    task_handler.send({f'{n}号任务'})
    n += 1

# TODO 错位获取next
# todo 用for实现
