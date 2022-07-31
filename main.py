from config import GAME_HEIGHT, GAME_WIDTH, SQUARE_SIZE
import pygame    
from model import SnakeModel, Direction
from draw import View

pygame.init()    
# done variable is using as flag     
done = False    
clock = pygame.time.Clock()

model = SnakeModel(GAME_HEIGHT, GAME_WIDTH)

# size variable is using for set screen size
  
size = [GAME_HEIGHT * SQUARE_SIZE, GAME_WIDTH * SQUARE_SIZE]    
screen = pygame.display.set_mode(size)    
pygame.display.set_caption("Snek")    

view = View(screen, SQUARE_SIZE)
view.draw(model)

while not done:
    # clock.tick() limits the while loop to a max of 10 times per second.    
    clock.tick(10)

    for event in pygame.event.get():  # User did something    
            if event.type == pygame.QUIT:  # If user clicked on close symbol     
                done = True  # done variable that we are complete, so we exit this loop    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and model.game_over:
                    model = SnakeModel(GAME_HEIGHT, GAME_WIDTH)
                    view.draw(model)
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