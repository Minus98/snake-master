import time
from agent import Agent
from agent_environment_interface import AgentEnvironmentInterface
from model import Direction
import numpy as np

environment = AgentEnvironmentInterface()
agent = Agent(0.99, 0.005, 1, 0.01)
scores = []
amount_of_steps = []
games = 50000
#state = environment.getState()

for i in range(games):

    state = environment.reset_environment()
    done = False
    steps = 0

    if i % 100 == 0 and i != 0:
        print("After", i, "games:")
        print("Current avg score: ", np.mean(scores[-100 :]))
        print("Current avg steps: ", np.mean(amount_of_steps[-100 :]))
        #print(agent.epsilon)

    while not done:
        
        action = agent.act(state)
        steps += 1
        state_, reward, done = environment.step(Direction(action))

        agent.store_transition(state, action, reward, state_, done)

        agent.learn()

        state = state_
    #print("Finished game", i + 1, "after", steps, "steps with score:", environment.getScore())
    scores.append(environment.getScore())
    amount_of_steps.append(steps)

print(scores)