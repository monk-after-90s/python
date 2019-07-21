import asyncio


async def big_coro():
    coros = []
    for s in ['A', 'B', 'C']:
        async def coro(s=s):
            print('{}号协程启动'.format(s))
            tasks = []
            for i in range(5):
                async def coro2(i=i):
                    print('{}号协程启动'.format(i))
                    await asyncio.sleep(2)
                    print('{}号协程结束'.format(i))

                tasks.append(coro2())
            await asyncio.wait(tasks)
            print('{}号协程结束'.format(s))

        coros.append(coro())
    await asyncio.wait(coros)


asyncio.run(big_coro())
