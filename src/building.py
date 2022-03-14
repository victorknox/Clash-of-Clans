import os
from colorama import Fore, Back, Style, init
import math

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
        self.content = [[Fore.GREEN + icon + Fore.RESET]*self.length for tile in range(self.height)]


    def attacked(self, damage):
        " receives damage and updates the health accordingly "
        self.health -= damage
        if self.health <= 0:
            self.destroy()
        elif self.health < self.maxhealth/5:
            self.update_color(Fore.RED)
        elif self.health < self.maxhealth/2:
            self.update_color(Fore.YELLOW)
        else:
            self.update_color(Fore.GREEN)
    
    def destroy(self):
        " destroys the building and updates the board accordingly "
        self.content = [['']*self.length for tile in range(self.height)]
        self.x = -1
        self.y = -1

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
    """ The Hut class which inherits from the Building class. It is the building which is the main target of the game. """
    def __init__(self, position):
        height = 1
        length = 1
        maxhealth = 100
        icon = 'H'
        super().__init__(height, length, position, maxhealth, icon)

class Wall(Building):
    """ The Wall class which inherits from the Building class. It is the building which is the main target of the game. """
    def __init__(self, position):
        height = 1
        length = 1
        maxhealth = 50
        icon = '#'
        super().__init__(height, length, position, maxhealth, icon)
        self.iswall = True
    
class Cannon(Building):
    """ The Cannon class which inherits from the Building class. It is the building which is the main target of the game. """
    def __init__(self, position):
        height = 2
        length = 2
        maxhealth = 200
        self.attack_range = 6
        self.damage = 10
        icon = 'C'
        super().__init__(height, length, position, maxhealth, icon)

    def attack_enemy(self, characters):
        """ This method is used to attack the enemy. It checks if the enemy is in the attack range and if so, it deals damage to the enemy. """
        x = self.x
        y = self.y
        inrange = False
        for character in characters:
            if character.x <= x + self.attack_range and character.x >= x - self.attack_range and character.y <= y + self.attack_range and character.y >= y - self.attack_range:
                character.attacked(self.damage)
                inrange = True
                break
        if not inrange:
            # change canon color to original color
            self.attacked(0)
        else:
            # change canon color to white to indicate attack
            self.update_color(Fore.WHITE)
        return

                


