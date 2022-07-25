import random
from enum import Enum 

class SnakeModel:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.game_over = False
        self.score = 0
        
        self.movement_locked = False

        #Throw exception if board too small in future
        start_x = random.randint(10, width-10)
        start_y = random.randint(10, height-10)

        self.snake = [Location(start_x, start_y)]
        self.current_direction = random.choice(list(Direction))

        self.generate_point()



    def step(self):

        current_head = self.snake[0]

        if(self.current_direction == Direction.UP):
            new_head = Location(current_head.x, current_head.y - 1)
        elif(self.current_direction == Direction.RIGHT):
            new_head = Location(current_head.x + 1, current_head.y)
        elif(self.current_direction == Direction.DOWN):
            new_head = Location(current_head.x, current_head.y + 1)
        elif(self.current_direction == Direction.LEFT):
            new_head = Location(current_head.x - 1, current_head.y)
        
        if (self.check_game_over(new_head)):
            self.game_over = True
            return
        
        self.snake.insert(0, new_head)

        if(new_head.collides(self.current_point_location)):
            self.score += 10
            self.generate_point()
        else:
            self.snake.pop()

        self.movement_locked = False
            

    def check_game_over(self, new_head):
        
        #Outside of screen
        if(new_head.x < 0 or new_head.x >= self.width or new_head.y < 0 or new_head.y >= self.height):
            return True
        
        for i in range(len(self.snake) - 1):
            if new_head.collides(self.snake[i]):
                return True

        return False

    def set_direction(self, direction):
        
        if(self.movement_locked):
            return

        if(direction == Direction.UP and self.current_direction == Direction.DOWN):
            return
        elif(direction == Direction.RIGHT and self.current_direction == Direction.LEFT):
            return
        elif(direction == Direction.DOWN and self.current_direction == Direction.UP):
            return
        elif(direction == Direction.LEFT and self.current_direction == Direction.RIGHT):
            return

        self.current_direction = direction
        self.movement_locked = True

    def generate_point(self):
        
        valid_location_found = False
        
        while not valid_location_found:
            
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            point_location = Location(x,y)

            valid_location_found = True
            for location in self.snake:
                if(point_location.collides(location)):
                    valid_location_found = False
                    break
        
        self.current_point_location = Location(x,y)



class Location:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def collides(self, other_location):
        return self.x == other_location.x and self.y == other_location.y

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4