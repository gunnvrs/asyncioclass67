# Thread version of cooking 1 kitchen 1 chefs 1 dishes
from time import time, ctime, sleep
from threading import Thread

def cooking(index):
    start_time = time()
    print(f'{ctime()} Kitchen-{index}   : Begin Cooking...')
    sleep(2)
    duration = time() - start_time
    print(f'{ctime()} Kitchen-{index}   : Cooking done in {duration:0.2f} seconds!')


if __name__ == "__main__":
    print(f'{ctime()} Main  : Starting cook.')
    start_time = time()

    index = 1
    c1 = Thread(target=cooking(index))
    c1.start()
    c1.join()

    duration = time() - start_time
    print(f"{ctime} Main    : Finished cooking duration in {duration:0.2f} seconds")