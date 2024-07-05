# synchronous breakfast
from time import sleep, time

def make_coffee():
    print("coffee: prepare ingridients")
    sleep(1)
    print("coffee: waiting...")
    sleep(5)
    print("coffee: ready")

def fry_eggs():
    print("eggs: prepare ingridients")
    sleep(1)
    print("eggs: frying...")
    sleep(3)
    print("eggs: ready")

def main():
    start = time()
    make_coffee()
    fry_eggs()
    print(f"breakfast is ready in {time()-start} min")


main()