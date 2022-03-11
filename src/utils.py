import os 
import colorama 
from src.building import *
from src.characters import *
from src.input import *
from src.board import *
from src.spells import *


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
        self.buildings = [TownHall((40, 12)), Hut((20, 18)), Hut((40, 10)), Hut((20, 15)), Hut((60, 10)), Hut((30, 18)), Hut((40, 18)), Cannon((20, 10)), Cannon((60, 16))]        
        # Initialize walls
        for x in range(15, 66):
            self.buildings.append(Wall((x, 8)))
            self.buildings.append(Wall((x, 20)))
        for y in range(8, 21):
            self.buildings.append(Wall((15, y)))
            self.buildings.append(Wall((65, y)))
        self.characters = [self.king]
        self.board.update(self.buildings, self.characters)
        
    def end_game(self):
        end = True
        for character in self.characters:
            if(character.health > 0):
                end = False
        if(end):
            print('DEFEAT!')
            exit()
        else:
            for building in self.buildings:
                if(isinstance(building, Wall) == False):
                    if(building.health > 0):
                        end = False
            if(end):
                print('VICTORY!')
                exit()
        

    def run_game(self):
        while(True):
            os.system('clear')
            self.board.display()
            ip = input_to()
            self.end_game()
            if(ip == 'q'):
                os.system('clear')
                exit() 
            if(ip == 's' or 'w' or 'a' or 'd'):
            # King moves
                self.king.move(ip, self.board)
            if(ip == ' '):
            # King attacks the building in front of him
                self.king.attack_enemy(self.buildings)
            if (ip == 'p' or 'i' or 'o'):
                # spawn a barbarian at the respective spawn point
                # spawn points are (2, 2), (22, 70), (2, 70)
                if(ip == 'i'):
                    self.characters.append(Barbarian((2, 2)))
                if(ip == 'o'):
                    self.characters.append(Barbarian((70, 22)))
                if(ip == 'p'):
                    self.characters.append(Barbarian((70, 2)))
            if (ip =='r'):
                pass
            if (ip == 'h'):
                pass
            # update the board in each iteration
            self.board.update(self.buildings, self.characters)

            