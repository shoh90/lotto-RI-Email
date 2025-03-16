import numpy as np

class LottoEnv:
    def __init__(self, past_data, n_numbers=45, n_select=6):
        self.past_data = past_data
        self.n_numbers = n_numbers
        self.n_select = n_select
        self.state = np.zeros(self.n_numbers)
    
    def reset(self):
        self.state = np.zeros(self.n_numbers)
        return self.state
    
    def step(self, action):
        reward = self.calculate_reward(action)
        return self.state, reward
    
    def calculate_reward(self, action):
        match_count = sum([1 for num in action if num in self.past_data])
        return match_count
