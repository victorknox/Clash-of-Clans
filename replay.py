import pickle
import sys
import time
from src.board import *

f = sys.argv[1]
pickle_off = open(f, "rb")
boards = pickle.load(pickle_off)

def main():
    for board in boards:
        # sleep for 0.01 second
        time.sleep(0.1)
        os.system('clear')
        board.display()

if __name__ == "__main__":
    main()