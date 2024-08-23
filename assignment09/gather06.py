# example of canceling all tasks if one task fails
import asyncio
 
# cancel all tasks except the current task
def cancel_all_tasks():
    # get all running tasks
    tasks = asyncio.all_tasks()
    # get the current task
    current = asyncio.current_task()
    # remove current task from all tasks
    tasks.remove(current)
    # cancel all remaining running tasks
    for task in tasks:
        task.cancel()
 
# coroutine used for a task
async def task_coro(value):
    # report a message
    print(f'>task {value} executing')
    # sleep for a moment
    await asyncio.sleep(1)
    # check if this task should fail
    if value == 5:
        print(f'>task {value} failing')
        raise Exception('Something bad happened')
    # otherwise, block again
    await asyncio.sleep(1)
    print(f'>task {value} done')
    return value
 
# coroutine used for the entry point
async def main():
    # create many coroutines
    coros = [task_coro(i) for i in range(10)]
    # execute all coroutines as a group
    group = asyncio.gather(*coros)
    # handle the case that a task fails
    try:
        # wait for the group of tasks to complete
        await group
    except Exception as e:
        # report failure
        print(f'A task failed with: {e}, canceling all tasks')
        # cancel all tasks
        cancel_all_tasks()
    # wait a while
    await asyncio.sleep(2)
 
# start the asyncio program
asyncio.run(main())