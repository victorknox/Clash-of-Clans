import os
from time import *
from colorama import Fore, Back, Style, init
from numpy import character

init()
size = os.get_terminal_size()

class Character:
    """ The Character class which stores basic details such as health, position, etc.
    also stores basic methods such and unit movement, taking damage attacking the enemy """

    def __init__(self, maxhealth, damage, position, ms, icon, c_range, aoe = 0):
        """ The Character class which stores basic details such as health, position, etc."""
        self.health = maxhealth
        self.maxhealth = maxhealth
        self.damage = damage
        self.ms = ms
        self.x = position[0]
        self.y = position[1]
        self.icon = icon
        self.c_range = c_range
        self.direction = "r"
        self.aoe = aoe
        self.aerial = False
        self.content = [[Fore.BLUE + icon + Fore.RESET]*1 for tile in range(1)]


    def unitmove(self, ip, board):
        """ Unit move for any character, checks if the unit can move in the direction it is facing and if it can, moves it. """
        # areal units ignore buildings and walls
        if self.aerial:
            if ip == 'w':
                self.y -= 1
            elif ip == 's':
                self.y += 1
            elif ip == 'a':
                self.x -= 1
            elif ip == 'd':
                self.x += 1
        else:
            if ip == 'w' and board.content[self.y-1][self.x] == ' ':
                self.y -= 1
            elif ip == 's' and board.content[self.y+1][self.x] == ' ':
                self.y += 1
            elif ip == 'a' and board.content[self.y][self.x-1] == ' ':
                self.x -= 1
            elif ip == 'd' and board.content[self.y][self.x+1] == ' ':
                self.x += 1
            else: 
                return -1
        return 1
            
    def automove(self, board, buildings):
        """ Character automove method, checks for the closest building and moves towards it. """
        
        # search for the closest building
        closest = -1

        # aerial character movement
        flag = False
        if self.aerial:
            for building in buildings:
                if building.damage > 0:
                    flag = True
                    break

        for building in buildings:
            if flag and self.aerial:
                if building.damage == 0:
                    continue
            if building.iswall == False:
                if closest == -1:
                    closest = building
                else:
                    if abs(self.x - building.x) + abs(self.y - building.y) < abs(self.x - closest.x) + abs(self.y - closest.y):
                        closest = building
        if closest == -1:
            return
        dist = self.distance_building(self.x, self.y, closest)
        # move towards closest buiding
        if dist > self.c_range:
            if closest.x > self.x:
                self.direction = "r"
                self.move(buildings, "d", board)
            elif closest.x < self.x:
                self.direction = "l"
                self.move(buildings, "a", board)
            elif closest.y > self.y:
                self.direction = "d"
                self.move(buildings, "s", board)
            elif closest.y < self.y:
                self.direction = "u"
                self.move(buildings, "w", board)
        else:
            self.attack_enemy(buildings)

    def distance_building(self, x, y, building):
        """ returns the distance between the unit and the building """
        curr_dist = 10000
        for i in range(building.length):
            for j in range(building.height):
                t = max(abs(x - building.x - i), abs(y - building.y - j))
                if t < curr_dist:
                    curr_dist = t
        return curr_dist
        

    def attack_enemy(self, buildings, wall = 0):
        """ Attack enemy method, checks if the unit can attack the enemy and if it can, attacks it. """
        a_range = self.c_range
        if wall == 1:
            a_range = 1
        for building in buildings:
            if wall == 0:
                if building.iswall == True:
                    continue
            if self.direction == "r":
                if(self.x + a_range >= building.x and self.y <= building.y + building.height - 1 and self.y >= building.y):
                    building.attacked(self.damage, buildings)
            elif self.direction == "l":
                if(self.x - a_range <= building.x + building.length - 1 and self.y <= building.y + building.height - 1 and self.y >= building.y):
                    building.attacked(self.damage, buildings)
            elif self.direction == "u":
                if(self.y - a_range <= building.y + building.height - 1 and self.x <= building.x + building.length - 1 and self.x >= building.x):
                    building.attacked(self.damage, buildings)
            elif self.direction == "d":
                if(self.y + a_range >= building.y and self.x <= building.x + building.length - 1 and self.x >= building.x):
                    building.attacked(self.damage, buildings)


    def attacked(self, damage, characters):
        """ receives damage and updates the health accordingly """
        self.health -= damage
        if self.health <= 0:
            self.destroy(characters)
        elif self.health <= self.maxhealth/4:
            self.update_color(Fore.WHITE)
        elif self.health <= self.maxhealth/2:
            self.update_color(Fore.CYAN)
        else:
            self.update_color(Fore.BLUE)
    
    def move(self, buildings, ip, board):
        """ Character move method, checks if the character can move in the direction it is facing and if it can, moves it. """
        val = self.unitmove(ip, board)
        if val == -1:
            self.attack_enemy(buildings, 1)

    def destroy(self, characters):
        """ removes the unit from the board """
        try:
            characters.remove(self)
        except:
            pass


    def update_color(self, color):
        """ updates the color of the unit """
        self.content = [[color + self.icon + Fore.RESET]*1 for tile in range(1)]

class Hero(Character): 
    """ Hero class, inherits from Character class. """
    def move(self, ip, board):
        """ Hero move method, checks if the hero can move in the direction it is facing and if it can, moves it. """
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

    def attack_enemy(self, buildings):
        """ Attack enemy method, checks if the unit can attack the enemy and if it can, attacks it. """
        x = self.x
        y = self.y
        if self.direction == "r":
            x += self.c_range
        elif self.direction == "l":
            x -= self.c_range
        elif self.direction == "u":
            y -= self.c_range
        elif self.direction == "d":
            y += self.c_range

        for building in buildings:
            dist = self.distance_building(x,y,building)
            if dist <= self.aoe:
                building.attacked(self.damage, buildings)

class King(Hero):
    """ King class, inherits from Character and Hero class """

    def __init__(self):
        """ initialize the king with basic details """
        health = 1000
        damage = 30
        position = (1, 1)
        ms = 1
        c_range = 1
        aoe = 0
        icon = '┼'
        super().__init__(health, damage, position, ms, icon, c_range, aoe)

    def special_attack(self, buildings):
        """ Axe attack method, attacks any building withing the radius of the attack range. """
        attack_range = 3
        for building in buildings:
            for i in range(-attack_range, attack_range):
                for j in range(-attack_range, attack_range):
                    if(self.x + i <= building.x + building.length - 1 and self.x + i >= building.x):
                        if(self.y + j <= building.y + building.height - 1 and self.y + j >= building.y):
                            building.attacked(self.damage, buildings)

class Queen(Hero):
    """ Queen class, inherits from Character and Hero class """
    def __init__(self):
        """ initialize the queen with basic details """
        health = 1000
        damage = 20
        position = (1, 1)
        ms = 1
        c_range = 8
        aoe = 2
        icon = 'q'
        super().__init__(health, damage, position, ms, icon, c_range, aoe)

    def special_attack(self, buildings):
        """ Eagle arrow method, attacks in a range with AOE damage. """
        self.c_range = 16
        self.aoe = 4
        self.attack_enemy(buildings)
        self.c_range = 8
        self.aoe = 2

class Barbarian(Character):
    """ Barbarian class, inherits from Character class """

    def __init__(self, position):
        """ initialize the barbarian with basic details """
        health = 300
        damage = 2
        ms = 1
        icon = '¥'
        c_range = 1
        super().__init__(health, damage, position, ms, icon, c_range)
        

class Archer(Character):
    """ Archer class, inherits from Character class """

    def __init__(self, position):
        """ initialize the archer with basic details """
        health = 150
        damage = 1
        ms = 2
        c_range = 5
        icon = '⚔'
        super().__init__(health, damage, position, ms, icon, c_range)

            
class Baloon(Character):
    """ Baloon class, inherits from Character class """

    def __init__(self, position):
        """ initialize the baloon with basic details """
        health = 300
        damage = 4
        ms = 2
        c_range = 0
        icon = 'o'
        super().__init__(health, damage, position, ms, icon, c_range)
        self.aerial = True

    def attack_enemy(self, buildings):
        for building in buildings:
            if self.distance_building(self.x, self.y, building) <= self.c_range:
                building.attacked(self.damage, buildings)


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
            self.move(buildings, "d", board)
        elif closest.x < self.x:
            self.direction = "l"
            self.move(buildings, "a", board)
        elif closest.y > self.y:
            self.direction = "d"
            self.move(buildings, "s", board)
        elif closest.y < self.y:
            self.direction = "u"
            self.move(buildings, "w", board)
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

