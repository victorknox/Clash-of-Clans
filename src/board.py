import os 
import math
import colorama 
from src.building import *
from src.characters import *

class Board: 
    def __init__(self):
        " initializing the board and setting the width and height with respect to the terminal "
        size = os.get_terminal_size()
        self.height = size.lines
        self.width = size.columns
        self.clear()

    def clear(self):
        
        # Blank board with boundaries
        self.content = [[' ']*self.width for tile in range(self.height)]
        self.content[0] = ['═']*self.width
        self.content[self.height-1] = ['═']*self.width
        for i in range(self.height): self.content[i][0] = '║'
        for i in range(self.height): self.content[i][self.width-1] = '║'
        self.content[0][0]='╔'
        self.content[0][self.width-1]='╗'
        self.content[self.height-1][0]='╚'
        self.content[self.height-1][self.width-1]='╝'

        # Initialize spawning points
        self.content[2][2] = Fore.YELLOW + 'I' + Fore.RESET
        self.content[self.height-3][self.width -3] = Fore.YELLOW + 'O' + Fore.RESET
        self.content[2][self.width -3] = Fore.YELLOW + 'P' + Fore.RESET


    def display(self):
        " displays the board "
        for row in self.content:
            print(''.join(row))

    def update(self, buildings, characters):
        " updates the board, with updated building and character parameters as input"
        self.clear()
        for building in buildings:
            for row in range(building.height):
                self.content[building.y + row][building.x: building.x + building.length] = building.content[row]
        for character in characters:
            self.content[character.y][character.x: character.x + 1] = character.content[0]
        