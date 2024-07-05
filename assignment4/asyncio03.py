# example of gather for many coroutines in a list
import asyncio

# coroutine for task
async def task_coro(value):
    #report a message
    print(f'>task {value} executing')
    #block for a moment
    await asyncio.sleep(1)

#coroutine 
async def main():
    #report a message
    print('main starting')

    coros = [task_coro(i) for i in range(10)]

    await asyncio.gather(*coros)

    print('main done')


asyncio.run(main())
