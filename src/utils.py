import os 
import pickle
from time import *
from datetime import datetime
from src.building import *
from src.characters import *
from src.input import *
from src.board import *
from src.spells import *
import copy


class Game():
    """ The Game class containing the main game loop, methods for initializing the game and ending the game """
    def __init__(self,level = 1):
        " Initialize the required objects for the game "
        self.board = Board()
        self.hero = King()
        self.buildings = []
        self.characters = []
        self.barbarian_limit = 6
        self.archer_limit = 6
        self.balloon_limit = 3
        self.barbarians = 0
        self.archers = 0
        self.balloons = 0
        self.boards = []
        self.input = input_to()
        self.level = level
        self.qattack = 0
        self.init_game()
        self.run_game()

    def init_game(self):
        " Initialize the game with the village and characters required at the starting point"

        # Initialize buildings, this defines the village structure at the beginning of game, More buildings are added per level
        self.buildings = [TownHall((40, 12)), Hut((20, 18)), Hut((20, 16)), Hut((22, 18)), Hut((22, 16)), Hut((20, 19)), Hut((22, 19)), Cannon((35, 12)), Cannon((60, 16)), WizardTower((20, 10)), WizardTower((47, 12))]        
        if self.level == 2:
            self.buildings.append(WizardTower((60, 12)))
            self.buildings.append(Cannon((47, 18)))
        if self.level == 3:
            self.buildings.append(WizardTower((60, 12)))
            self.buildings.append(WizardTower((35, 16)))
            self.buildings.append(Cannon((47, 16)))
            self.buildings.append(Cannon((22, 14)))
        
        # Initialize walls
        for x in range(15, 66):
            self.buildings.append(Wall((x, 8)))
            self.buildings.append(Wall((x, 20)))
        for y in range(8, 21):
            self.buildings.append(Wall((15, y)))
            self.buildings.append(Wall((65, y)))
        
        # Initialize the Hero, player gets to choose between King and Queen
        if self.level == 1:
            while(1):
                h = input("Enter k for King, q for Queen: ")
                if h == "k":
                    break
                elif h == "q":
                    self.hero = Queen()
                    break
                else:
                    print("Incorrect input")
        self.characters = [self.hero]
        self.board.update(self.buildings, self.characters)

    def check_loss(self):
        # Declare it a loss if all the characters on the board are dead
        loss = True
        for character in self.characters:
            if(character.health > 0):
                loss = False
        if(loss):
            print("Defeat!")
            self.save_game()
            exit()
        
    def check_win(self):    
        # Declare it a win if all the buildings on the board are destroyed. 
        win = True
        for building in self.buildings:
            if(building.iswall == False):
                if(building.health > 0):
                    win = False
        if(win):
            return 1
        else:
            return 0

    def end_game(self):
        """Checks if the round or game is over, if the round is won, player proceeds to next round."""
        
        self.check_loss()
        # if previous round is won, move to next round
        if self.check_win() == 1:
            if self.level <= 2:
                print("Victory!\n Next Round")
                sleep(3)
                self.level += 1
                self.board = Board()
                self.buildings = []
                self.characters = []
                self.barbarian_limit = 6
                self.archer_limit = 6
                self.balloon_limit = 3
                self.barbarians = 0
                self.archers = 0
                self.balloons = 0
                self.boards = []
                self.hero.health = self.hero.maxhealth
                self.input = input_to()
                self.init_game()
                self.run_game()

            else:
                print("You have won the game!")
                exit()
            

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

            # Hero moves
            if(ip == 's' or 'w' or 'a' or 'd'):
                self.hero.move(ip, self.board)

            # Hero attacks the building in front of them
            if(ip == ' '):
                self.hero.attack_enemy(self.buildings)

            # Hero uses the special attack 
            
            # In case of the queens attack, there's a time delay before the attack is executed
            if(self.qattack >= time() - 1):
                self.hero.special_attack(self.buildings)
                self.qattack = 0

            if (ip == 'e'):
                if isinstance(self.hero, King):
                    self.hero.special_attack(self.buildings)
                elif isinstance(self.hero, Queen) and self.qattack == 0:
                    self.qattack = time()

            # spawn a troop at the respective spawn point
            if (ip == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9'):
                # spawn points are (2, 2), (70, 22), (70, 2), they can be accessed through the numbers 1 to 9
                p1 = (2, 2)
                p2 = (70, 22)
                p3 = (70, 2)
                if(len(self.characters ) <= self.barbarian_limit + self.archer_limit + self.balloon_limit):
                    if(ip == '1' and self.barbarians < self.barbarian_limit):
                        self.characters.append(Barbarian(p1))
                        self.barbarians += 1
                    if(ip == '2' and self.barbarians < self.barbarian_limit):
                        self.characters.append(Barbarian(p2))
                        self.barbarians += 1
                    if(ip == '3' and self.barbarians < self.barbarian_limit):
                        self.characters.append(Barbarian(p3))
                        self.barbarians += 1
                    if(ip == '4' and self.archers < self.archer_limit):
                        self.characters.append(Archer(p1))
                        self.archers += 1
                    if(ip == '5' and self.archers < self.archer_limit):
                        self.characters.append(Archer(p2))
                        self.archers += 1
                    if(ip == '6' and self.archers < self.archer_limit):
                        self.characters.append(Archer(p3))
                        self.archers += 1
                    if(ip == '7' and self.balloons < self.balloon_limit):
                        self.characters.append(Baloon(p1))
                        self.balloons += 1
                    if(ip == '8' and self.balloons < self.balloon_limit):
                        self.characters.append(Baloon(p2))
                        self.balloons += 1
                    if(ip == '9' and self.balloons < self.balloon_limit):
                        self.characters.append(Baloon(p3))
                        self.balloons += 1
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

            