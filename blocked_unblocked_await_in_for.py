import asyncio
import time


async def slow_main():
    print(f'{slow_main.__name__} start time:{time.strftime("%X")}')
    # tasks = []
    for i in range(5):
        a = await asyncio.sleep(1)
        print(a)

    # for task in tasks:
    #     await task
    print(f'end time:{time.strftime("%X")}')


async def fast_main(mode=1):
    print(f'{fast_main.__name__} start time:{time.strftime("%X")}')
    tasks = []
    for i in range(5):
        tasks.append(asyncio.create_task(asyncio.sleep(1)))

    await asyncio.wait(tasks)
    if mode == 1:
        for task in tasks:
            a = await task
            print(a)
    elif mode == 2:
        await asyncio.wait(tasks)
    print(f'end time:{time.strftime("%X")}')


async def main():
    await fast_main()
    await slow_main()


asyncio.run(main())
