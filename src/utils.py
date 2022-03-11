import os 
import colorama 
from src.building import *
from src.characters import *
from src.input import *
from src.board import *

class Game:

    def __init__(self):
        self.board = Board()
        self.king = King()
        self.buildings = []
        self.characters = []
        self.input = input_to()
        self.init_game()
        self.run_game()

    def init_game(self):
        
        # Initialize buildings and Characters
        self.buildings = [TownHall((40, 12)), Hut((20, 18)), Hut((40, 10)), Hut((20, 15)), Hut((60, 10)), Hut((20, 10)), Hut((60, 16)), Cannon((20, 10)), Cannon((60, 16))]        
        # Initialize walls
        for x in range(15, 66):
            self.buildings.append(Wall((x, 8)))
            self.buildings.append(Wall((x, 20)))
        for y in range(8, 21):
            self.buildings.append(Wall((15, y)))
            self.buildings.append(Wall((65, y)))
        self.characters = [self.king]
        self.board.update(self.buildings, self.characters)
        

    def run_game(self):
        while(True):
            os.system('clear')
            self.board.display()
            ip = input_to()
            if(ip == 'q'):
                os.system('clear')
                exit() 
            if(ip == 's' or 'w' or 'a' or 'd'):
            # King moves
                self.king.move(ip, self.board)
            if(ip == ' '):
            # King attacks the building right to him
                for building in self.buildings:
                    if(self.king.x + 1 == building.x and self.king.y <= building.y + building.height - 1 and self.king.y >= building.y):
                        self.king.attack_enemy(building)
            if (ip == 'p' or 'i' or 'o'):
                pass
            else:
                pass
            # update the board in each iteration
            self.board.update(self.buildings, self.characters)
            # canon attack
            for building in self.buildings:
                if(isinstance(building, Cannon)):
                    building.attack_enemy(self.characters)

            