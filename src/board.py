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

        # Blank board with boundaries
        self.content = [[' ']*self.width for tile in range(self.height)]
        self.content[0] = ['#']*self.width
        self.content[self.height-1] = ['#']*self.width
        for i in range(self.height): self.content[i][0] = '#'
        for i in range(self.height): self.content[i][self.width-1] = '#'

        # Initialize spawning points
        self.content[2][2] = Fore.YELLOW + 'I' + Fore.RESET
        self.content[self.height-3][self.width -3] = Fore.YELLOW + 'O' + Fore.RESET
        self.content[2][self.width -3] = Fore.YELLOW + 'P' + Fore.RESET
        
        # Initialize buildings and Characters
        self.buildings = [TownHall((40, 12)), Hut((20, 18)), Hut((40, 10)), Hut((20, 15)), Hut((60, 10)), Cannon((20, 10)), Cannon((60, 16))]
        # Initialize walls
        for x in range(15, 70):
            self.buildings.append(Wall((x, 8)))
            self.buildings.append(Wall((x, 20)))
        for y in range(8, 21):
            self.buildings.append(Wall((15, y)))
            self.buildings.append(Wall((70, y)))
        self.characters = []
        self.update(self.buildings, self.characters)



    def display(self):
        " displays the board "
        for row in self.content:
            print(''.join(row))

    def update(self, buildings, characters):
        " updates the board, with updated building and character parameters as input"
        for building in buildings:
            for row in range(building.height):
                self.content[building.y + row][building.x: building.x + building.length] = building.content[row]
        for character in characters:
            self.content[character.y][character.x] = character.content

        # for row in range(building.height):
        #     for col in range(building.length):
        #         self.content[building.y + row][building.x + col] = building.content[row][col]
        # for row in range(building.height):
        #     for col in range(building.length):
        #         self.content[building.y + row][building.x + col] = building.content[row][col]