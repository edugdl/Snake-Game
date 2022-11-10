class SnakeBody:
    def __init__(self, position, map_grid, child):
        self.position = position
        self.map_grid = map_grid
        self.child = child
        self.parent = None

    def get_position(self):
        return self.position

    def move(self, new_position):

        if self.child:
            self.child.move(self.position[:])
        else:
            self.map_grid[self.position[1]][self.position[0]] = ''
        self.position = new_position
        self.map_grid[self.position[1]][self.position[0]] = self

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def get_direction(self):
        x_p, y_p = self.parent.get_position()
        x, y = self.get_position()
        return [x_p - x, y_p - y]

    def grow(self):
        if self.child:
            self.child.grow()
        else:
            self.child = SnakeBody(self.position[:], self.map_grid, None)
            self.child.set_parent(self)


class SnakeHead(SnakeBody):
    def __init__(self, position, map_grid, child):
        super().__init__(position, map_grid, child)
        self.score = 0
        self.direction = [0, 0]

    def get_direction(self):
        return self.direction

    def move(self, direction):
        if direction == [0, 0]:
            self.map_grid[self.position[1]][self.position[0]] = self
            return True
        self.child.move(self.position[:])
        self.position[0] += direction[0]
        self.position[1] += direction[1]
        self.direction = direction
        if self.detect_collision():
            return False
        if "Fruit" in str(type(self.map_grid[self.position[1]][self.position[0]])):
            self.map_grid[self.position[1]][self.position[0]].got_eaten()
            self.grow()
        self.map_grid[self.position[1]][self.position[0]] = self
        return True

    def detect_collision(self):
        if self.position[1] > 15 or self.position[0] > 15:
            return True
        elif self.position[1] < 0 or self.position[0] < 0:
            return True
        elif "Snake" in str(type(self.map_grid[self.position[1]][self.position[0]])) and not self.direction == [0, 0]:
            return True
        return False