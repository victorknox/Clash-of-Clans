import os
from colorama import Fore, Back, Style, init

init()
size = os.get_terminal_size()

class Character:
    def __init__(self, health, damage, position, ms, icon):
        self.health = health
        self.damage = damage
        self.ms = ms
        self.x = position[0]
        self.y = position[1]
        self.icon = icon
        self.content = [[Fore.BLUE + icon + Fore.RESET]*1 for tile in range(1)]


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
        elif self.health <= 200:
            self.update_color(Fore.CYAN)
        elif self.health <= 100:
            self.update_color(Fore.WHITE)
        else:
            self.update_color(Fore.BLUE)

    def destroy(self):
        self.content = [[Fore.RED + 'x' + Fore.RESET]*1 for tile in range(1)]
        self.x = -1
        self.y = -1

    def update_color(self, color):
        self.content = [[color + self.icon + Fore.RESET]*1 for tile in range(1)]



class King(Character):
    def __init__(self):
        health = 1000
        damage = 30
        position = (1, 1)
        ms = 1
        icon = '┼'
        super().__init__(health, damage, position, ms, icon)
        

class Barbarian(Character):
    def __init__(self, position):
        health = 300
        damage = 1
        ms = 1
        icon = '¥'
        super().__init__(health, damage, position, ms, icon)

    def automove(self, board, buildings):
        # find closest buiding
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
            self.move('d', board)
        elif closest.x < self.x:
            self.move('a', board)
        elif closest.y > self.y:
            self.move('s', board)
        elif closest.y < self.y:
            self.move('w', board)
        else:
            pass

