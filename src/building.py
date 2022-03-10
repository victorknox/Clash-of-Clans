import os
from colorama import Fore, Back, Style, init

init()

class Building:
    def __init__(self, height, length, position, health):
        self.health = health
        self.height = height
        self.length = length
        self.x = position[0]
        self.y = position[1]

    def attacked(self):
        self.health -= 1
        if self.health == 0:
            self.destroy()
    
    def destroy(self):
        self.content = [[' ']*self.length for tile in range(self.height)]

    def update_color(self, color):
        for row in self.content:
            for i in range(len(row)):
                row[i] = color + row[i] + Fore.RESET

# class SpawningPoint(Building):
#     def __init__(self, height, length, position, health):
#         height = 1
#         length = 1
#         health = 50
#         super().__init__(height, length, position, health)
#         self.content = [[Fore.GREEN + 'S']*self.length for tile in range(self.height)]

class TownHall(Building):
    def __init__(self, position):
        height = 4
        length = 3
        health = 1000
        super().__init__(height, length, position, health)
        self.content = [[Fore.GREEN + 'T' + Fore.RESET]*self.length for tile in range(self.height)]

class Hut(Building):
    def __init__(self, position):
        height = 1
        length = 1
        health = 100
        super().__init__(height, length, position, health)
        self.content = [[Fore.GREEN + 'H' + Fore.RESET]*self.length for tile in range(self.height)]

class Wall(Building):
    def __init__(self, position):
        height = 1
        length = 1
        health = 50
        super().__init__(height, length, position, health)
        self.content = [['#' + Fore.RESET]*self.length for tile in range(self.height)]
    
class Cannon(Building):
    def __init__(self, position):
        height = 2
        length = 2
        health = 300
        # range = 6
        damage = 50
        super().__init__(height, length, position, health)
        self.content = [[Fore.GREEN + 'C' + Fore.RESET]*self.length for tile in range(self.height)]
