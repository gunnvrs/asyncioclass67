# example of getting the current task from the main coroutine
import asyncio

#define a main coroutine 
async def main():
    #report message
    print('main coroutine started')
    #get the current task
    task = asyncio.current_task()
    #report its details
    print(task)

asyncio.run(main())