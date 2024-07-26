import asyncio
import time

my_compute_time = 0.1
opponent_compute_time = 0.5
opponnents = 24
move_pairs = 30

#don't forget to declare the main() dunc as a async func
async def main(x):
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        # print(f"BOARD-{x+1} {i+1} Judit made a move.")
        # dont use time.sleep in a async function. im using it because in reality you aren't thniking about making a
        # move on 24 boards at the same time, and so I need to block event loop
        time.sleep(my_compute_time)
        print(f"BOARD-{x+1} {i+1} Judit made a move.")
        # here our opponent is making their turn and now we can move onto the next board.
        await asyncio.sleep(opponent_compute_time)
        print(f"BOARD-{x+1} {i+1} Opponent made move.")
    print(f"BOARD-{x+1} - >>>>>>>>>>>>>>>> Finished move in {round(time.perf_counter() - board_start_time)} secs\n")
    return round(time.perf_counter() - board_start_time)

async def async_io():
    # again same structure as in async-io.py
    tasks = []
    for i in range(opponnents):
        tasks += [main(i)]
    await asyncio.gather(*tasks)
    print(f"Board exhibition finished in{round(time.perf_counter() - start_time)} secs.")

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(async_io())
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")



