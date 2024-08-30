from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue):
    producer_start_time = time.perf_counter()
    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = i
        # block to simulate work
        sleeptime = random()
        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    print('Producer: Done')
    print(f"Producer finished in {round(time.perf_counter() - producer_start_time, 2)} secs\n")

# coroutine to consume work
async def consumer(queue):
    consumer_start_time = time.perf_counter()
    print('Consumer: Running')
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    # all done
    print('Consumer: Done')
    print(f"Consumer finished in {round(time.perf_counter() - consumer_start_time, 2)} secs\n")

# entry point coroutine
async def main():
    # measure total time
    total_start_time = time.perf_counter()

    # create the shared queue
    queue = asyncio.Queue()
    
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

    # measure total elapsed time
    total_time = round(time.perf_counter() - total_start_time, 2)
    print(f"\nTotal time to complete both: {total_time} secs")

# start the asyncio program
asyncio.run(main())
