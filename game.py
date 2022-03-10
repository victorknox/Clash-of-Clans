import os
import random 
from src.board import *
from src.building import *
from src.input import *
from src.characters import *

def main(): 
    king = King()
    board = Board()
    while(True):
        os.system('clear')
        board.display()
        ip = input_to()
        if(ip == 'q'):
            os.system('clear')
            exit() 
        if(ip == 's' or 'w' or 'a' or 'd'):
            king.move(ip)
        else:
            print(ip)
            print("Invalid Move!")
            # pass





if __name__ == "__main__":
    main()