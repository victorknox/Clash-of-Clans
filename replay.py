import pickle
import sys
import time
from src.board import *

# taking input from user for replay
f = sys.argv[1]
pickle_off = open(f, "rb")
boards = pickle.load(pickle_off)

def main():
    # display each frame of the board with a time delay of 0.1 seconds
    for board in boards:
        time.sleep(0.1)
        os.system('clear')
        board.display()

if __name__ == "__main__":
    main()