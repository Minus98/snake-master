import pygame    
from model import SnakeModel, Direction
from draw import View

pygame.init()    
# done variable is using as flag     
done = False    
clock = pygame.time.Clock()

game_height = 25
game_width = 25 

model = SnakeModel(game_height, game_width)

# size variable is using for set screen size
square_size = 40    
size = [game_height * square_size, game_width * square_size]    
screen = pygame.display.set_mode(size)    
pygame.display.set_caption("Example program to draw geometry")    

view = View(screen, square_size)
view.draw(model)

while not done:
    # clock.tick() limits the while loop to a max of 10 times per second.    
    clock.tick(10)

    for event in pygame.event.get():  # User did something    
            if event.type == pygame.QUIT:  # If user clicked on close symbol     
                done = True  # done variable that we are complete, so we exit this loop    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    model.set_direction(Direction.UP)
                elif event.key == pygame.K_RIGHT:
                    model.set_direction(Direction.RIGHT)
                elif event.key == pygame.K_DOWN:
                    model.set_direction(Direction.DOWN)
                elif event.key == pygame.K_LEFT:
                    model.set_direction(Direction.LEFT)

    if not model.game_over:
        
        model.step()
        view.draw(model)
        # All drawing code occurs after the for loop and but    
        # inside the main while done==False loop.    

# Quit the execution when clicking on close    
pygame.quit()    