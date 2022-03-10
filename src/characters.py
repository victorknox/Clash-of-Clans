import os
from colorama import Fore, Back, Style, init

init()

class Character:
    def __init__(self, health, attack, position, ms):
        self.health = health
        self.attack = attack
        self.ms = ms
        self.x = position[0]
        self.y = position[1]
            
    def move(self, ip, board):
        if ip == 'w' and self.y > 1:
            self.y = max(self.y - self.ms, 1)
        elif ip == 's' and self.y < os.get_terminal_size().lines - 2:
            self.y = min(self.y + self.ms, os.get_terminal_size().lines - 2)
        elif ip == 'a' and self.x > 1:
            self.x = max(self.x - self.ms, 1)
        elif ip == 'd' and self.x < os.get_terminal_size().columns - 2: 
            self.x = min(self.x + self.ms, os.get_terminal_size().columns - 2)
        else:
            pass

    def attack_enemy(self, enemy, attack):
        enemy.health -= attack
        if enemy.health <= 0:
            enemy.alive = False


class King(Character):
    def __init__(self):
        health = 100
        attack = 10
        position = (1, 1)
        ms = 2
        super().__init__(health, attack, position, ms)
        self.content = [[Fore.RED + 'K' + Fore.RESET]*1 for tile in range(1)]
        

    def attack_enemy(self, enemy, attack):
        enemy.health -= attack
        if enemy.health <= 0:
            enemy.alive = False


