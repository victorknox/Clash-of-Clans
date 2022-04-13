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
        
        # Initializing a Blank board with boundaries
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
        self.content[22][70] = Fore.YELLOW + 'O' + Fore.RESET
        self.content[2][70] = Fore.YELLOW + 'P' + Fore.RESET

    def display(self):
        " displays the board "
        for row in self.content[:-1]:
            print(''.join(row))
        print(''.join(self.content[-1]), end = '')

    def update(self, buildings, characters):
        " updates the board, with updated building and character parameters as input"
        self.clear()
        # updating each building
        for building in buildings:
            for row in range(building.height):
                self.content[building.y + row][building.x: building.x + building.length] = building.content[row]
        
        # updating each character
        for character in characters:
            self.content[character.y][character.x: character.x + 1] = character.content[0]
        
        # updating Hero's health bar
        self.content[1][self.width-13]='H'
        self.content[1][self.width-12]=':'
        for i in range(math.floor(characters[0].health/100)):
            self.content[1][self.width-11+i]= Fore.CYAN + '■' + Fore.RESET

        # updating the troops on board
        self.content[1][self.width-25]='T'
        self.content[1][self.width-24]=':'
        self.content[1][self.width-23]= str(len(characters))
        
        # defensive buildings attacking enemies
        for building in buildings:
            if(isinstance(building, Cannon)):
                building.attack_enemy(buildings, characters)
            elif(isinstance(building, WizardTower)):
                building.attack_enemy(buildings, characters)

        # calling all characters' automated movement
        for character in characters[1:]:
            for i in range(character.ms):
                character.automove(self, buildings)
