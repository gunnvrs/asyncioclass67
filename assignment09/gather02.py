# example of gather with of tasks and coroutines
import asyncio
 
# coroutine used for a task
async def task_coro(value):
    # report a message
    print(f'>task {value} executing')
    # sleep for a moment
    await asyncio.sleep(1)
 
# coroutine used for the entry point
async def main():
    # report a message
    print('main starting')
    # create a mix of awaitables
    awaitables = [task_coro(0),
        asyncio.create_task(task_coro(1)),
        task_coro(2),
        asyncio.create_task(task_coro(3)),
        task_coro(4),]
    # schedule the group
    _ = asyncio.gather(*awaitables)
    # wait around for a while
    await asyncio.sleep(2)
    # report a message
    print('main done')
 
# start the asyncio program
asyncio.run(main())