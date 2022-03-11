import os
from colorama import Fore, Back, Style, init

init()
size = os.get_terminal_size()

class Character:
    def __init__(self, health, damage, position, ms):
        self.health = health
        self.damage = damage
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
        enemy.attacked(self.damage)
    
    def attacked(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.destroy()
        # elif self.health < self.maxhealth/5:
        #     self.update_color(Fore.RED)
        # elif self.health < self.maxhealth/2:
        #     self.update_color(Fore.YELLOW)
        # else:
        #     self.update_color(Fore.GREEN)

    def destroy(self):
        self.content = [[' ']*1 for tile in range(1)]
        self.x = -1
        self.y = -1

    # def update_color(self, color):
    #     for row in range(self.height):
    #         for col in range(self.length):
    #             self.content[row][col] = color + self.icon + Fore.RESET



class King(Character):
    def __init__(self):
        health = 1000
        damage = 30
        position = (1, 1)
        ms = 1
        super().__init__(health, damage, position, ms)
        self.content = [[Fore.MAGENTA + '┼' + Fore.RESET]*1 for tile in range(1)]
        

class Barbarian(Character):
    def __init__(self, position):
        health = 20
        damage = 10
        ms = 1
        super().__init__(health, damage, position, ms)
        self.content = [[Fore.RED + '¥' + Fore.RESET]*1 for tile in range(1)]
