import os
import time
from colorama import Fore, Back, Style, init

init()
size = os.get_terminal_size()

class Character:
    """ The Character class which stores basic details such as health, position, etc.
    also stores basic methods such and unit movement, taking damage attacking the enemy """

    def __init__(self, maxhealth, damage, position, ms, icon):
        """ The Character class which stores basic details such as health, position, etc."""
        self.health = maxhealth
        self.maxhealth = maxhealth
        self.damage = damage
        self.ms = ms
        self.x = position[0]
        self.y = position[1]
        self.icon = icon
        self.direction = "r"
        self.content = [[Fore.BLUE + icon + Fore.RESET]*1 for tile in range(1)]


    def unitmove(self, ip, board):
        """ Unit move for any character, checks if the unit can move in the direction it is facing and if it can, moves it. """
        if ip == 'w' and board.content[self.y-1][self.x] == ' ':
            self.y -= 1
        elif ip == 's' and board.content[self.y+1][self.x] == ' ':
            self.y += 1
        elif ip == 'a' and board.content[self.y][self.x-1] == ' ':
            self.x -= 1
        elif ip == 'd' and board.content[self.y][self.x+1] == ' ':
            self.x += 1
        else:
            pass        

    def attack_enemy(self, buildings):
        """ Attack enemy method, checks if the unit can attack the enemy and if it can, attacks it. """
        for building in buildings:
            if self.direction == "r":
                if(self.x + 1 == building.x and self.y <= building.y + building.height - 1 and self.y >= building.y):
                    building.attacked(self.damage)
            elif self.direction == "l":
                if(self.x - 1 == building.x + building.length - 1 and self.y <= building.y + building.height - 1 and self.y >= building.y):
                    building.attacked(self.damage)
            elif self.direction == "u":
                if(self.y - 1 == building.y + building.height - 1 and self.x <= building.x + building.length - 1 and self.x >= building.x):
                    building.attacked(self.damage)
            elif self.direction == "d":
                if(self.y + 1 == building.y and self.x <= building.x + building.length - 1 and self.x >= building.x):
                    building.attacked(self.damage)

    def attacked(self, damage):
        """ receives damage and updates the health accordingly """
        self.health -= damage
        if self.health <= 0:
            self.destroy()
        elif self.health <= self.maxhealth/4:
            self.update_color(Fore.WHITE)
        elif self.health <= self.maxhealth/2:
            self.update_color(Fore.CYAN)
        else:
            self.update_color(Fore.BLUE)

    def destroy(self):
        """ removes the unit from the board """
        self.content = [['' + Fore.RESET]*1 for tile in range(1)]
        self.x = -1
        self.y = -1


    def update_color(self, color):
        """ updates the color of the unit """
        self.content = [[color + self.icon + Fore.RESET]*1 for tile in range(1)]



class King(Character):
    """ King class, inherits from Character class """

    def __init__(self):
        """ initialize the king with basic details """
        health = 1000
        damage = 30
        position = (1, 1)
        ms = 1
        icon = '┼'
        super().__init__(health, damage, position, ms, icon)

    def move(self, ip, board):
        """ King move method, checks if the king can move in the direction it is facing and if it can, moves it. """
        if ip == 'w':
            self.direction = "u"
        elif ip == 's':
            self.direction = "d"
        elif ip == 'a':
            self.direction = "l"
        elif ip == 'd':
            self.direction = "r"
        ms = self.ms
        while(ms > 0):
            self.unitmove(ip, board)
            ms -= 1

    def axe_attack(self, buildings):
        """ Axe attack method, attacks any building withing the radius of the attack range. """
        attack_range = 3
        for building in buildings:
            for i in range(-attack_range, attack_range):
                for j in range(-attack_range, attack_range):
                    if(self.x + i <= building.x + building.length - 1 and self.x + i >= building.x):
                        if(self.y + j <= building.y + building.height - 1 and self.y + j >= building.y):
                            building.attacked(self.damage)


class Barbarian(Character):
    """ Barbarian class, inherits from Character class """

    def __init__(self, position):
        """ initialize the barbarian with basic details """
        health = 300
        damage = 1
        ms = 1
        icon = '¥'
        super().__init__(health, damage, position, ms, icon)

    def automove(self, board, buildings):
        """ Barbarian automove method, checks for the closest building and moves towards it. """
        
        # search for the closest building
        closest = -1
        for building in buildings:
            if building.iswall == False:
                if closest == -1:
                    closest = building
                else:
                    if abs(self.x - building.x) + abs(self.y - building.y) < abs(self.x - closest.x) + abs(self.y - closest.y):
                        closest = building
        
        # move towards closest buiding
        if closest.x > self.x:
            self.direction = "r"
            self.move("d", board)
        elif closest.x < self.x:
            self.direction = "l"
            self.move("a", board)
        elif closest.y > self.y:
            self.direction = "d"
            self.move("s", board)
        elif closest.y < self.y:
            self.direction = "u"
            self.move("w", board)
        else:
            pass
        self.attack_enemy(buildings)

    def move(self, ip, board):
        """ Barbarian move method, checks if the barbarian can move in the direction it is facing and if it can, moves it. """
        ms = self.ms
        while(ms > 0):
            self.unitmove(ip, board)
            ms -= 1

class Wallbreaker(Character):
    """ Wallbreaker class, inherits from Character class """

    def __init__(self, position):
        """ initialize the wallbreaker with basic details """
        health = 100
        damage = 1000
        ms = 2
        icon = '¤'
        super().__init__(health, damage, position, ms, icon)

    def bomb_attack(self, buildings):
        """ Bomb attack method, attacks any building withing the radius of the attack range. """
        attack_range = 3
        for building in buildings:
            for i in range(-attack_range, attack_range):
                for j in range(-attack_range, attack_range):
                    if(self.x + i <= building.x + building.length - 1 and self.x + i >= building.x):
                        if(self.y + j <= building.y + building.height - 1 and self.y + j >= building.y):
                            building.attacked(self.damage)

    def automove(self, board, buildings):
        """ Wallbreaker automove method, checks for the closest wall and moves towards it. """
        
        # search for the closest wall
        closest = -1
        for building in buildings:
            if building.iswall == True:
                if closest == -1:
                    closest = building
                else:
                    if abs(self.x - building.x) + abs(self.y - building.y) < abs(self.x - closest.x) + abs(self.y - closest.y):
                        closest = building

        # move towards closest wall
        if closest.x > self.x:
            self.direction = "r"
            self.move("d", board)
        elif closest.x < self.x:
            self.direction = "l"
            self.move("a", board)
        elif closest.y > self.y:
            self.direction = "d"
            self.move("s", board)
        elif closest.y < self.y:
            self.direction = "u"
            self.move("w", board)
        else:
            pass
        for building in buildings:
            if building.iswall == True:
                if abs(self.x - building.x) + abs(self.y - building.y) <= 1:
                    self.bomb_attack(buildings)
                    self.destroy()

    def move(self, ip, board):
        """ Wallbreaker move method, checks if the wallbreaker can move in the direction it is facing and if it can, moves it. """
        ms = self.ms
        while(ms > 0):
            self.unitmove(ip, board)
            ms -= 1
