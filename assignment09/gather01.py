# example of gather for many coroutines that return values
import asyncio
 
# coroutine used for a task
async def task_coro(value):
    # report a message
    print(f'>task {value} executing')
    # sleep for a moment
    await asyncio.sleep(1)
    # return a value
    return value * 10
 
# coroutine used for the entry point
async def main():
    # report a message
    print('main starting')
    # create many tasks
    tasks = [task_coro(i) for i in range(10)]
    # run the tasks
    values = await asyncio.gather(*tasks)
    # report the values
    print(values)
    # report a message
    print('main done')
 
# start the asyncio program
asyncio.run(main())