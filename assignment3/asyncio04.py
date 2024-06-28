from time import ctime
import asyncio

async def wash(basket):
    print(f'{ctime()}   : Washing Machine ({basket}): Put the coin')
    print(f'{ctime()}   : Washing Machine ({basket}): Start washing...')
    await asyncio.sleep(5)
    print(f'{ctime()}   : Washing Machine ({basket}): Finished washing')
    return f'{ctime()}   : {basket} is completed'

async def main():
    # create coroutine
    coro = wash('Basket A')
    print(f"{ctime()}   : {coro}")
    print(f'{ctime()}   : {type(coro)}')
    # create task
    task = asyncio.create_task(coro)
    print(f"{ctime()}   : {task}")
    print(f"{ctime()}   : {type(task)}")
    #
    result = await task
    print(f"{ctime()}   : {result}")

if __name__ == '__main__':
    asyncio.run(main())
