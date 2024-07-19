import time

class Coffee:
    pass

class Egg:
    pass

class Bacon:
    pass

class Toast:
    pass

class Juice:
    pass

def PourCoffee():
    print(f'{time.ctime()} - Begin pour coffee...')
    time.sleep(2)
    print(f'{time.ctime()} - Finish pour coffee...')
    return Coffee()

def ApplyButter():
    print(f'{time.ctime()} - Begin apply butter...')
    time.sleep(1)
    print(f'{time.ctime()} - Finish apply butter...')

def FryEggs (eggs) :
    print(f'{time.ctime()} - Begin fry eggs...')
    print (f'{time.ctime()} - Heat pan to fry eggs') 
    time.sleep(1)

    for egg in range (eggs):
        print(f' {time. ctime()} - Frying', egg+1, 'eggs')
        time.sleep (1)
    print(f'{time.ctime()} - Finish fry eggs...')
    print(f'{time.ctime()} - >>>>>>>> Fry eggs are ready...')
    return Egg()

def FryBacon():
    print(f"{time.ctime()} - Begin fry bacon...")
    time.sleep(2)
    print(f'{time.ctime()} - Finish fry bacon...')
    print(f'{time.ctime()} - >>>>>>>> Fry bacon is ready...')
    return Bacon ()

def ToastBread(slices):
    for slice in range(slices) :
        print(f' {time.ctime()} - Toasting bread', slice + 1)
        time.sleep(1)
        print(f'{time.ctime()} - Bread', slice + 1, 'toasted' )
        ApplyButter()
        print (f'{time.ctime()} - Toast', slice + 1, 'ready')
    print(f'{time.ctime()} - ›>>>>>>> Toast are ready\n' )
    return Toast()

def PourJuice():
    print(f'{time.ctime()} - Begin pour joice...')
    time.sleep (1)
    print(f'{time.ctime()} - Finish pour joice...')
    return Juice()

def main():
    PourCoffee()
    print(f'{time.ctime()} - >>>>>>>> Coffee is ready\n')
    FryEggs (2)
    FryBacon()
    ToastBread (2)
    print (f'\n{time.ctime()} - >>>>>>>> Nearly to finished...')
    PourJuice ()

if __name__== '__main__':
    start_cooking = time.perf_counter()
    ### start run main
    main()
    elapsed = time.perf_counter() - start_cooking
    print(f"{time.ctime()} - Breakfast cooked in ", elapsed, "seconds.")

    