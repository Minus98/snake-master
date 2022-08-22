from collections import deque, namedtuple
import random
from turtle import forward
from agent_environment_interface import AgentEnvironmentInterface
from config import GAME_HEIGHT, GAME_WIDTH, SQUARE_SIZE
from dqn import ConvDeepQNetwork
from model import Direction
import numpy as np
import torch as T


class Agent():

    def __init__(self, gamma, alpha, epsilon_start, epsilon_min):
        
        self.gamma = gamma
        self.alpha = alpha
        self.epsilon = epsilon_start
        self.epsilon_min = epsilon_min

        self.dqn = ConvDeepQNetwork(GAME_HEIGHT * SQUARE_SIZE, GAME_WIDTH * SQUARE_SIZE, 4, alpha)

        self.memory = ReplayMemory(1000, (3, GAME_HEIGHT * SQUARE_SIZE, GAME_WIDTH * SQUARE_SIZE))
        self.batch_size=32


    def act(self, state):

        sample = random.random()

        if sample > self.epsilon:
            tensor_state = T.tensor(state).to(self.dqn.device).float().unsqueeze(0)
            actions = self.dqn.forward(tensor_state)
            action = T.argmax(actions).item()
        else:
            action = random.randrange(4)

        return action

    def learn(self):

        if self.epsilon > self.epsilon_min:
            self.epsilon *= 0.999

        if self.memory.counter < self.batch_size:
            return

        self.dqn.optimizer.zero_grad()

        max_mem = min (self.memory.counter, self.memory.size)

        batch = np.random.choice(max_mem, self.batch_size, replace=False)

        batch_index = np.arange(self.batch_size, dtype=np.int32)

        state_batch = T.tensor(self.memory.state_memory[batch]).to(self.dqn.device)
        new_state_batch = T.tensor(self.memory.new_state_memory[batch]).to(self.dqn.device)
        reward_batch = T.tensor(self.memory.reward_memory[batch]).to(self.dqn.device)
        terminal_batch = T.tensor(self.memory.terminal_memory[batch]).to(self.dqn.device)

        action_batch = self.memory.action_memory[batch]
        q_eval = self.dqn.forward(state_batch)[batch_index, action_batch]
        q_next = self.dqn.forward(new_state_batch)
        q_next[terminal_batch] = 0.0

        q_target = reward_batch + self.gamma * T.max(q_next, dim=1)[0]

        loss = self.dqn.loss(q_target, q_eval).to(self.dqn.device)
        loss.backward()
        self.dqn.optimizer.step()

    def store_transition(self, state, action, reward, new_state, done):
        self.memory.store_transition(state, action, reward, new_state, done)

class ReplayMemory():

    def __init__(self, size, input_dims):

        self.counter = 0
        self.size = size

        self.state_memory = np.zeros((size, *input_dims), dtype=np.float32)
        self.new_state_memory = np.zeros((size, *input_dims), dtype=np.float32)
        self.action_memory = np.zeros(size, dtype=np.int32)
        self.reward_memory = np.zeros(size, dtype=np.float32)
        self.terminal_memory = np.zeros(size, dtype=bool)

    def store_transition(self, state, action, reward, new_state, done):

        index = self.counter % self.size
        self.state_memory[index] = state
        self.new_state_memory[index] = new_state
        self.action_memory[index] = action
        self.reward_memory[index] = reward
        self.terminal_memory[index] = done

        self.counter += 1


Agent(0.99, 0.01, 0.8, 0.05)