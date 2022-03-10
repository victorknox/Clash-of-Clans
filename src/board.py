import os 
# import colorama 


class Board: 
    def __init__(self):
        size = os.get_terminal_size()
        self.height = size.lines
        self.width = size.columns
        self.clear()

    def clear(self):
        self.content = [[' ']*self.width for tile in range(self.height)]
        # Add Horizontal Boundaries
        self.content[0] = ['#']*self.width
        self.content[self.height-1] = ['#']*self.width
        # Add Vertical Boundaries
        for i in range(self.height): self.content[i][0] = '#'
        for i in range(self.height): self.content[i][self.width-1] = '#'

    def display(self):
        for row in self.content:
            print(''.join(row))

    def update(self, building):
        for row in range(building.height):
            self.content[building.y + row][building.x: building.x + building.length] = building.content[row]
        # for row in range(building.height):
        #     for col in range(building.length):
        #         self.content[building.y + row][building.x + col] = building.content[row][col]
        # for row in range(building.height):
        #     for col in range(building.length):
        #         self.content[building.y + row][building.x + col] = building.content[row][col]