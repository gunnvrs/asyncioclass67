# example of gather where one task is canceled with returned exceptions
import asyncio
 
# coroutine used for a task
async def task_coro(value, friend):
    # report a message
    print(f'>task {value} executing')
    # cancel friend task
    if friend:
        friend.cancel()
    # sleep for a moment
    await asyncio.sleep(1)
 
# coroutine used for the entry point
async def main():
    # report a message
    print('main starting')
    # create many tasks
    task0 = asyncio.create_task(task_coro(0, None))
    task1 = asyncio.create_task(task_coro(1, task0))
    # run the tasks
    results = await asyncio.gather(task0, task1, return_exceptions=True)
    # report results
    print(results)
    # report a message
    print('main done')
 
# start the asyncio program
asyncio.run(main())