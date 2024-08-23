# example of asyncio task group with return values
import asyncio

# coroutine task
async def task(value):
    # sleep to simulate waiting
    await asyncio.sleep(1)
    # return value
    return value * 100

# asyncio entry point
async def main():
    # create task group
    async with asyncio.TaskGroup() as group:
        # create and issue tasks
        tasks = [group.create_task(task(i)) for i in range(1,10)]
    # wait for ali tasks to complete...
    # report all results
    for t in tasks:
        print(t.result())

# entry point
asyncio.run(main())