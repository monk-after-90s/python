import asyncio


async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3)
    print('yay!')


async def main():
    # Wait for at most 1 second
    realtask = asyncio.create_task(eternity())
    shiled_coro = asyncio.shield(realtask)
    try:
        await asyncio.wait_for(shiled_coro, timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')
    await realtask


asyncio.run(main())
