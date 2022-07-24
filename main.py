import pygame    
from model import SnakeModel, Direction
from draw import View

pygame.init()    
# done variable is using as flag     
done = False    
clock = pygame.time.Clock()

game_height = 30
game_width = 30 

model = SnakeModel(game_height, game_width)

# size variable is using for set screen size
square_size = 20    
size = [game_height * square_size, game_width * square_size]    
screen = pygame.display.set_mode(size)    
pygame.display.set_caption("Example program to draw geometry")    

view = View(screen, square_size)
view.draw(model)

def handle_input(model):
    keys = pygame.key.get_pressed()  
    # It will manage the keys movement for the snake  
    if keys[pygame.K_LEFT]:  
        model.set_direction(Direction.LEFT)
    elif keys[pygame.K_RIGHT]:  
        model.set_direction(Direction.RIGHT) 
    elif keys[pygame.K_UP]:  
        model.set_direction(Direction.UP)
    elif keys[pygame.K_DOWN]:  
        model.set_direction(Direction.DOWN)

while not done:
    # clock.tick() limits the while loop to a max of 10 times per second.    
    clock.tick(10)

    handle_input(model)

    for event in pygame.event.get():  # User did something    
            if event.type == pygame.QUIT:  # If user clicked on close symbol     
                done = True  # done variable that we are complete, so we exit this loop    

    if not model.game_over:
        
        model.step()
        view.draw(model)
        # All drawing code occurs after the for loop and but    
        # inside the main while done==False loop.    

# Quit the execution when clicking on close    
pygame.quit()    