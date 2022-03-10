import os
from colorama import Fore, Back, Style, init

init()
size = os.get_terminal_size()

class Character:
    def __init__(self, health, attack, position, ms):
        self.health = health
        self.attack = attack
        self.ms = ms
        self.x = position[0]
        self.y = position[1]
            
    def move(self, ip, board):
        ms = self.ms
        while(ms > 0):
            self.unitmove(ip, board)
            ms -= 1

    def unitmove(self, ip, board):
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

    def attack_enemy(self, enemy):
        enemy.attacked(self.attack)



class King(Character):
    def __init__(self):
        health = 100
        attack = 20
        position = (1, 1)
        ms = 1
        super().__init__(health, attack, position, ms)
        self.content = [[Fore.RED + '┼' + Fore.RESET]*1 for tile in range(1)]
        


