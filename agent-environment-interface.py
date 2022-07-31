from config import GAME_HEIGHT, GAME_WIDTH, SQUARE_SIZE
from os import stat
from draw import View
from model import SnakeModel
import pygame   
import numpy as np

class AgentEnvironmentInterface:

    def __init__(self):

        pygame.init()
        size = [GAME_HEIGHT * SQUARE_SIZE, GAME_WIDTH * SQUARE_SIZE]    
        self.screen = pygame.display.set_mode(size)
        self.view = View(self.screen, SQUARE_SIZE)
        self.model = None

    def step(self, action):
        self.model.set_direction(action)

        score_before = self.model.score

        self.model.step()
        self.view.draw(self.model)

        reward = self.model.score - score_before
        state = self.getState()

        return state, reward
    
    def reset_environment(self):

        self.model = SnakeModel(GAME_HEIGHT,GAME_WIDTH)  
        self.view.draw(self.model)

        return self.getState()

    def getState(self):
        return np.array((pygame.surfarray.array3d(self.screen)))

AgentEnvironmentInterface()