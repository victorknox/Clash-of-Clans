import os
from colorama import Fore, Back, Style, init

init()



class Building:
    def __init__(self, height, length, health):
        self.health = health
        self.height = height
        self.length = length
        self.content = [[Fore.GREEN + 'X']*self.length for tile in range(self.height)]

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

class Spawn(Building):
    def __init__(self, height, length, health):
        super().__init__(height, length, health)
        self.content = [[Fore.BLUE + 'S']*self.length for tile in range(self.height)]

class TownHall(Building):
    def __init__(self, height, length, health):
        super().__init__(height, length, health)
        self.content = [[Fore.YELLOW + 'T']*self.length for tile in range(self.height)]

class Hut(Building):
    def __init__(self, height, length, health):
        super().__init__(height, length, health)
        self.content = [[Fore.RED + 'H']*self.length for tile in range(self.height)]

class Wall(Building):
    def __init__(self, height, length, health):
        super().__init__(height, length, health)
        self.content = [['X']*self.length for tile in range(self.height)]