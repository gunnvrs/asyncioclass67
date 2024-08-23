# example of gather with returned exceptions
import asyncio
 
# coroutine used for a task
async def task_coro(value):
    # report a message
    print(f'>task {value} executing')
    # sleep for a moment
    await asyncio.sleep(1)
    # check for failure
    if value == 0:
        raise Exception('Something bad happened')
    return value
 
# coroutine used for the entry point
async def main():
    # report a message
    print('main starting')
    # create many coroutines
    coros = [task_coro(i) for i in range(10)]
    # run the tasks
    results = await asyncio.gather(*coros, return_exceptions=True)
    # report results
    print(results)
    # report a message
    print('main done')
 
# start the asyncio program
asyncio.run(main())