from dqn import ConvDeepQNetwork


class Agent():

    def __init__(self, gamma, epsilon, alpha):
        
        self.value_network = ConvDeepQNetwork()