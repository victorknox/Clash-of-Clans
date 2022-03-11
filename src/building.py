import os
from colorama import Fore, Back, Style, init
import math

init(autoreset=True)

class Building:
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
        self.content = [[' ']*self.length for tile in range(self.height)]
        self.x = -1
        self.y = -1

    def update_color(self, color):
        for row in range(self.height):
            for col in range(self.length):
                self.content[row][col] = color + self.icon + Fore.RESET

class TownHall(Building):
    def __init__(self, position):
        height = 4
        length = 3
        maxhealth = 500
        icon = 'T'
        super().__init__(height, length, position, maxhealth, icon)

class Hut(Building):
    def __init__(self, position):
        height = 1
        length = 1
        maxhealth = 100
        icon = 'H'
        super().__init__(height, length, position, maxhealth, icon)

class Wall(Building):
    def __init__(self, position):
        height = 1
        length = 1
        maxhealth = 50
        icon = '#'
        super().__init__(height, length, position, maxhealth, icon)
        self.iswall = True
    
class Cannon(Building):
    def __init__(self, position):
        height = 2
        length = 2
        maxhealth = 200
        self.attack_range = 6
        self.damage = 10
        icon = 'C'
        super().__init__(height, length, position, maxhealth, icon)

    def attack_enemy(self, characters):
        # scan the range, if enemy is in range, attack
        x = self.x
        y = self.y
        inrange = False
        for character in characters:
            if character.x <= x + self.attack_range and character.x >= x - self.attack_range and character.y <= y + self.attack_range and character.y >= y - self.attack_range:
                character.attacked(self.damage)
                inrange = True
                break
        if not inrange:
            # change canon color
            self.attacked(0)
        else:
            # change canon color
            self.update_color(Fore.WHITE)
        return

                


