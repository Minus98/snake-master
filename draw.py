import pygame

class View:

    def __init__(self, screen, square_size):
        self.screen = screen
        self.square_size = square_size

    def draw(self, model):

        # Clear the default screen background and set the white screen background    
        self.screen.fill((255, 255, 255))    
    
        for location in model.snake:
            # Draw a rectangle outline    
            pygame.draw.rect(self.screen, (0, 0, 0), [location.x * self.square_size, location.y * self.square_size, self.square_size, self.square_size])    

        location = model.current_point_location
        pygame.draw.rect(self.screen, (0, 255, 0), [location.x * self.square_size, location.y * self.square_size, self.square_size, self.square_size])

        if(model.game_over):
            font = pygame.font.Font('freesansbold.ttf', 32)
            game_over_text = font.render('Game Over', True, (0,0,0))

            textRect = game_over_text.get_rect()
            w, h = pygame.display.get_surface().get_size()
            textRect.center = ( w // 2, h // 2)

            self.screen.blit(game_over_text, textRect)
        # This function must write after all the other drawing commands.    
        pygame.display.flip()