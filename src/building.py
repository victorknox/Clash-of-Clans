import os
from colorama import Fore, Back, Style, init
import math

from time import * 
from .characters import King

init(autoreset=True)

class Building:
    """ The Building parent class which stores basic details such as building size, health, position, etc.
    It also contains basic methods such as recieving damage, self destruction and updating the color of the building as the health drops. """
    
    def __init__(self, height, length, position, maxhealth, icon):
        self.health = maxhealth
        self.maxhealth = maxhealth
        self.height = height
        self.length = length
        self.icon = icon
        self.x = position[0]
        self.y = position[1]
        self.iswall = False
        self.damage = 0
        self.content = [[Fore.GREEN + icon + Fore.RESET]*self.length for tile in range(self.height)]


    def attacked(self, damage, buildings):
        " receives damage and updates the health accordingly "
        self.health -= damage
        if self.health <= 0:
            self.destroy(buildings)
        elif self.health < self.maxhealth/5:
            self.update_color(Fore.RED)
        elif self.health < self.maxhealth/2:
            self.update_color(Fore.YELLOW)
        else:
            self.update_color(Fore.GREEN)
    
    def destroy(self, buildings):
        " destroys the building and updates the board accordingly "
        try:
            buildings.remove(self)
        except:
            pass

    def update_color(self, color):
        " updates the color of the building "
        for row in range(self.height):
            for col in range(self.length):
                self.content[row][col] = color + self.icon + Fore.RESET

class TownHall(Building):
    """ The TownHall class which inherits from the Building class. It is the building which is the main target of the game. """
    def __init__(self, position, maxhealth):
        Building.__init__(self, 3, 3, position, maxhealth, 'T')
    def __init__(self, position):
        height = 4
        length = 3
        maxhealth = 500
        icon = 'T'
        super().__init__(height, length, position, maxhealth, icon)

class Hut(Building):
    """ The Hut class which inherits from the Building class. It is a normal building"""
    def __init__(self, position):
        height = 1
        length = 1
        maxhealth = 100
        icon = 'H'
        super().__init__(height, length, position, maxhealth, icon)

class Wall(Building):
    """ The Wall class which inherits from the Building class. It is a protective building around village"""
    def __init__(self, position):
        height = 1
        length = 1
        maxhealth = 50
        icon = '#'
        super().__init__(height, length, position, maxhealth, icon)
        self.iswall = True
    
class Cannon(Building):
    """ The Cannon class which inherits from the Building class. This is a defensive building which can attack the enemy """
    def __init__(self, position):
        height = 2
        length = 2
        maxhealth = 200
        self.attack_range = 6
        icon = 'C'
        super().__init__(height, length, position, maxhealth, icon)
        self.damage = 10

    def attack_enemy(self, buildings, characters):
        """ This method is used to attack the enemy. It checks if the enemy is in the attack range and if so, it deals damage to the enemy. """
        x = self.x
        y = self.y
        inrange = False
        for character in characters:
            if character.aerial:
                continue
            if character.x <= x + self.attack_range and character.x >= x - self.attack_range and character.y <= y + self.attack_range and character.y >= y - self.attack_range:
                character.attacked(self.damage, characters)
                inrange = True
                break
        if not inrange:
            # change canon color to original color
            self.attacked(0, buildings)
        else:
            # change canon color to white to indicate that it is attacking
            self.update_color(Fore.WHITE)
        return

class WizardTower(Building):
    """ The WizardTower class which inherits from the Building class. This is a defensive building which can attack the enemy, including areal ones """
    def __init__(self, position):
        height = 2
        length = 2
        maxhealth = 200
        self.attack_range = 6
        icon = 'W'
        super().__init__(height, length, position, maxhealth, icon)
        self.damage = 10
        self.aoe = 1

    # finds distance between tower and character
    def distance_character(self, x,y,character):
        dist = max(abs(character.x - x), abs(character.y - y))
        return dist

    def attack_enemy(self, buildings, characters):
        """ This method is used to attack the enemy. It checks if the enemy is in the attack range and if so, it deals damage to the enemy. This attack deals AOE damage to all characters in the area. """
        x = self.x
        y = self.y
        a_x = x
        a_y = y
        inrange = False
        for character in characters:
            if character.x <= x + self.attack_range and character.x >= x - self.attack_range and character.y <= y + self.attack_range and character.y >= y - self.attack_range:
                a_x = character.x
                a_y = character.y
                inrange = True
                break
        if not inrange:
            # change tower color to original color
            self.attacked(0, buildings)
        else:
            # change tower color to white to indicate attack
            self.update_color(Fore.WHITE)
            for character in characters:
                if self.distance_character(a_x, a_y, character) <= self.aoe:
                    character.attacked(self.damage, characters)

        return             


