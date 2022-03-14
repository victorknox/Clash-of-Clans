import os 
import pickle
from datetime import datetime
from src.building import *
from src.characters import *
from src.input import *
from src.board import *
from src.spells import *
import copy


class Game:
    """ The Game class containing the main game loop, methods for initializing the game and ending the game """
    def __init__(self):
        " Initialize the required objects for the game "
        self.board = Board()
        self.king = King()
        self.buildings = []
        self.characters = []
        self.barb_limit = 20
        self.boards = []
        self.input = input_to()
        self.init_game()
        self.run_game()

    def init_game(self):
        " Initialize the game with the village and characters required at the starting point"
        # Initialize buildings, this defines the village structure at the beginning of game
        self.buildings = [TownHall((40, 12)), Hut((20, 18)), Hut((40, 10)), Hut((20, 15)), Hut((60, 10)), Hut((30, 18)), Hut((40, 18)), Cannon((20, 10)), Cannon((60, 16))]        
        # Initialize walls
        for x in range(15, 66):
            self.buildings.append(Wall((x, 8)))
            self.buildings.append(Wall((x, 20)))
        for y in range(8, 21):
            self.buildings.append(Wall((15, y)))
            self.buildings.append(Wall((65, y)))
        # Initialize the King
        self.characters = [self.king]
        self.board.update(self.buildings, self.characters)


    def check_win(self):
        # Declare it a loss if all the characters on the board are dead
        win = True
        for character in self.characters:
            if(character.health > 0):
                win = False
        if(win):
            print("Defeat!")
            self.save_game()
            exit()
        
    def check_loss(self):    
        # Declare it a win if all the buildings on the board are destroyed. 
        loss = True
        for building in self.buildings:
            if(building.iswall == False):
                if(building.health > 0):
                    loss = False
        if(loss):
            print("Victory!")
            self.save_game()
            exit()

    def end_game(self):
        # check if the game is over
        self.check_win()
        self.check_loss()

    def save_game(self):
        # save the game to a pickle file, which contains all the instances of the board and characters
        now = datetime.now()
        dt_string = now.strftime("%d%m%Y%H%M")
        file_name = './replays/' + dt_string + '.pkl'
        with open(file_name, 'wb') as f:
            pickle.dump(self.boards, f)

    def run_game(self):
        # The main game loop
        while(True):
            
            # display the board and save it to the boards list
            os.system('clear')
            self.board.display()
            self.boards.append(copy.deepcopy(self.board))
            
            # take input from user
            ip = input_to()
            
            # quit the game if the user input is q
            if(ip == 'q'):
                os.system('clear')
                self.save_game()
                exit() 

            # King moves
            if(ip == 's' or 'w' or 'a' or 'd'):
                self.king.move(ip, self.board)

            # King attacks the building in front of him
            if(ip == ' '):
                self.king.attack_enemy(self.buildings)

            # King uses the axe attack 
            if (ip == 'e'):
                self.king.axe_attack(self.buildings)

            # spawn a barbarian at the respective spawn point
            if (ip == 'p' or 'i' or 'o' or 'u'):
                # spawn points are (2, 2), (22, 70), (2, 70) and (22, 2) (last one spawns a wallbreaker)
                if(len(self.characters ) < self.barb_limit + 1):
                    if(ip == 'i'):
                        self.characters.append(Barbarian((2, 2)))
                    if(ip == 'o'):
                        self.characters.append(Barbarian((70, 22)))
                    if(ip == 'p'):
                        self.characters.append(Barbarian((70, 2)))
                    if(ip == 'u'):
                        self.characters.append(Wallbreaker((2, 22))) 
                else:
                    pass

            # rage and heal spells
            if (ip =='r'):
                Rage(self.characters)
            if (ip == 'h'):
                Heal(self.characters)

            # update the board 
            self.board.update(self.buildings, self.characters)
            
            # check if the game is over 
            self.end_game()

            