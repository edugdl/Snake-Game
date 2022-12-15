class SnakeBody:
    def __init__(self, position, map_grid, child):
        self.position = position
        self.map_grid = map_grid
        self.child = child
        self.parent = None
        self.direction = [0,0]

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position[:]

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

    def set_child(self, child):
        self.child = child
    
    def get_child(self):
        return self.child

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
            self.score += 1
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

    def get_map_str(self):
        map = ""
        for row in self.map_grid:
            map+=str(row)+"\n"
        return map

class SwapSnake(SnakeHead):
    def __init__(self, position, map_grid, child):
        super().__init__(position, map_grid, child)
        self.next_move = [0,0]
    
    def grow(self):
        tail = self.get_tail()
        head_direction = tail.get_direction()[:]
        
        current_body = self.child
        tail.set_parent(current_body)
        current_body.set_parent(current_body.get_child())
        current_body.set_child(tail)
        last_body = current_body

        while True:
            if last_body.get_parent() == last_body.get_child():
                last_body.set_parent(self)
                break
            body = last_body.get_parent()
            last_child = body.get_child()
            body.set_child(body.get_parent())
            body.set_parent(last_child)
            if body.get_parent() == tail:
                body.set_parent(self)
                self.child = body
                break
            last_body = body

        temp = tail.get_position()[:]
        tail.set_position(self.position)
        self.position = temp
        self.direction = [head_direction[0] * -1, head_direction[1] * -1]
        self.child.grow()

    def get_tail(self):
        tail = self.child
        while tail.child:
            tail = tail.child
        return tail

    def get_next_move(self):
        return self.direction


        
