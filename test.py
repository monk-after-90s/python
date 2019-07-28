import asyncio
import time


async def async_generator(sleep_sec: int):
    while True:
        yield f'{sleep_sec} seconds'
        await asyncio.sleep(sleep_sec)





async def coro():
    as_gen1 = async_generator(1)
    as_gen2 = async_generator(2)

    async def anext_handle(as_gen):
        next = await as_gen.__anext__()
        print(f'{str(as_gen)}生成{next}')

    while True:
        await asyncio.gather(anext_handle(as_gen1), anext_handle(as_gen2))


asyncio.get_event_loop().run_until_complete(coro())
