import pygame

class View:

    def __init__(self, screen, square_size):
        self.screen = screen
        self.square_size = square_size

    def draw(self, model):

        # Clear the default screen background and set the white screen background    
        self.screen.fill((255, 255, 255))    
    
        for i in range(len(model.snake)):
            # Draw a rectangle outline
            location = model.snake[i]
            if i == 0:
                color = (0, 100, 0)
            else:
                color = (125, 125, 125)

            pygame.draw.rect(self.screen, color, [location.x * self.square_size, location.y * self.square_size, self.square_size, self.square_size])    

        location = model.current_point_location
        pygame.draw.rect(self.screen, (0, 255, 0), [location.x * self.square_size, location.y * self.square_size, self.square_size, self.square_size])

        font = pygame.font.Font('freesansbold.ttf', 32)

        w, h = pygame.display.get_surface().get_size()

        if(model.game_over):
            game_over_text = font.render('Game Over', True, (255,0,0))

            game_over_text_rect = game_over_text.get_rect()
            game_over_text_rect.center = ( w // 2, h // 2)

            self.screen.blit(game_over_text, game_over_text_rect)
        # This function must write after all the other drawing commands.    

        score_text = font.render('Score: ' + str(model.score), True, (0,128,0))
        score_text_rect = score_text.get_rect()
        score_text_rect.topright = (w, 0)
        self.screen.blit(score_text, score_text_rect)

        pygame.display.flip()