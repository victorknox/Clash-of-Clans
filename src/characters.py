import os
from colorama import Fore, Back, Style, init

init()
size = os.get_terminal_size()

class Character:
    def __init__(self, maxhealth, damage, position, ms, icon):
        self.health = maxhealth
        self.maxhealth = maxhealth
        self.damage = damage
        self.ms = ms
        self.x = position[0]
        self.y = position[1]
        self.icon = icon
        self.direction = "r"
        self.content = [[Fore.BLUE + icon + Fore.RESET]*1 for tile in range(1)]


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


    def attacked(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.destroy()
        elif self.health <= self.maxhealth/4:
            self.update_color(Fore.WHITE)
        elif self.health <= self.maxhealth/2:
            self.update_color(Fore.CYAN)
        else:
            self.update_color(Fore.BLUE)

    def destroy(self):
        self.content = [['' + Fore.RESET]*1 for tile in range(1)]
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

    def move(self, ip, board):
        # setting the character direction according to the input
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
        attack_range = 3
        for building in buildings:
            for i in range(-attack_range, attack_range):
                for j in range(-attack_range, attack_range):
                    if(self.x + i <= building.x + building.length - 1 and self.x + i >= building.x):
                        if(self.y + j <= building.y + building.height - 1 and self.y + j >= building.y):
                            building.attacked(self.damage)


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
            self.direction = "r"
            self.move("d", board)
        elif closest.x < self.x:
            self.direction = "l"
            self.move("a", board)
        elif closest.y > self.y:
            self.direction = "d"
            self.move("s", board)
        elif closest.y < self.y:
            self.direction = "u"
            self.move("w", board)
        else:
            pass
        self.attack_enemy(buildings)

    def move(self, ip, board):
        ms = self.ms
        while(ms > 0):
            self.unitmove(ip, board)
            ms -= 1

    def attack_enemy(self, buildings):
        for building in buildings:
            if self.direction == "r":
                if(self.x + 1 == building.x and self.y <= building.y + building.height - 1 and self.y >= building.y):
                    building.attacked(self.damage)
            elif self.direction == "l":
                if(self.x - 1 == building.x + building.length - 1 and self.y <= building.y + building.height - 1 and self.y >= building.y):
                    building.attacked(self.damage)
            elif self.direction == "u":
                if(self.y - 1 == building.y + building.height - 1 and self.x <= building.x + building.length - 1 and self.x >= building.x):
                    building.attacked(self.damage)
            elif self.direction == "d":
                if(self.y + 1 == building.y and self.x <= building.x + building.length - 1 and self.x >= building.x):
                    building.attacked(self.damage)
        

