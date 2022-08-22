from config import GAME_HEIGHT, GAME_WIDTH, SQUARE_SIZE
from draw import View
from model import SnakeModel
import pygame   
import numpy as np

class AgentEnvironmentInterface:

    def __init__(self):

        pygame.init()
        size = [GAME_WIDTH * SQUARE_SIZE, GAME_HEIGHT * SQUARE_SIZE]    
        self.screen = pygame.display.set_mode(size)
        self.view = View(self.screen, SQUARE_SIZE)
        self.reset_environment()

    def step(self, action):

        self.model.set_direction(action)

        score_before = self.model.score

        self.model.step()
        self.view.draw(self.model, False)

        reward = self.model.score - score_before
        state = self.getState()
        done = self.model.game_over

        return state, reward, done
    
    def reset_environment(self):

        self.model = SnakeModel(GAME_HEIGHT,GAME_WIDTH)  
        self.view.draw(self.model, False)

        return self.getState()

    def getState(self):
        return np.array((pygame.surfarray.array3d(self.screen))).transpose()

    def isDone(self):
        return self.model.game_over

    def getScore(self):
        return self.model.score