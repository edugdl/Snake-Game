from random import randint

class Fruit:
    def __init__(self, map_grid):
        self.eaten = True
        self.map_grid = map_grid
        self.x = None
        self.y = None
    
    def generate(self):
        if not self.eaten:
            return False
        self.eaten = False
        x = randint(0,15)
        y = randint(0,15)
        while self.map_grid[x][y] != '':
            x = randint(0,15)
            y = randint(0,15)
        self.map_grid[x][y] = self
        self.x, self.y = x,y
        return True

    def got_eaten(self):
        self.eaten = True
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
