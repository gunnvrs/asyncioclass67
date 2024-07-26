import time

my_compute_time = 0.1
opponent_compute_time = 0.5
opponnents = 3
move_pairs = 30

def game(x):
    #loop 30 times to simulate both players making a move
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        #print(f"BOARD-{x} {1+1} Judit thinking of making a move.")
        # we think for 5 sec
        time.sleep(my_compute_time)
        print(f"BOARD-{x+1} {i+1} Judit made a move.")
        #opponent thinks for 5 sec
        time.sleep(opponent_compute_time)
        print(f"BOARD-{x+1} {i+1} Opponent made move.")
    print(f"BOARD-{x+1} - >>>>>>>>>>>>>>>> Finished move in {round(time.perf_counter() - board_start_time)}")
    return round(time.perf_counter() - board_start_time)

if __name__ == "__main__": 
    start_time = time.perf_counter()
    # loops 24 times because we are playing with 24 opponent
    board_time = 0
    for board in range(opponnents):
        board_time += game(board)
    
    print(f"Board exhibition finished in {board_time} secs.")
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")
        

