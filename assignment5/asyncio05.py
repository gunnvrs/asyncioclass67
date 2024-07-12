from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(dish):
    # generate a random cooking time between 1 and 2 seconds
    value = 1 + random()

    print(f'Microwave ({dish}): Cooking {value} seconds...')
    # block for the specified time
    await asyncio.sleep(value)
    
    print(f'Microwave ({dish}): Finished cooking')

    return [dish, value]

# main coroutine
async def main():
    menu = ['rice', 'noodle', 'curry']
    # create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in menu]

    # wait for all tasks to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    print(f'Completed task: {len(done)}')

    completed = done.pop().result()
    # print(completed[0], completed[1])
    
    # get the first completed task result
    # completed_task = list(done)[0]
    # completed_dish, completed_time = completed_task.result()

    # # print results
    # print(f'Microwave ({completed[0], completed[1]}): Finished cooking')
    # print(f'Completed task: {len(completed)}')
    print(f'- {completed[0]} is completed in {completed[1]} seconds')
    print(f'Uncompleted task: {len(pending)}')

# start the asyncio program
asyncio.run(main())
