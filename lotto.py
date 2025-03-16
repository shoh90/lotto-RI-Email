import numpy as np
import random
import pickle

class LottoEnvRL:
    def __init__(self, past_data, n_numbers=45, n_select=6):
        self.past_data = past_data
        self.n_numbers = n_numbers
        self.n_select = n_select
        self.state = np.zeros(self.n_numbers)
        self.q_table = np.zeros((self.n_numbers, self.n_numbers))
    
    def reset(self):
        self.state = np.zeros(self.n_numbers)
        return self.state

    def step(self, action):
        reward = self.calculate_reward(action)
        return self.state, reward

    def calculate_reward(self, action):
        """과거 데이터와 비교하여 보상 계산"""
        match_count = sum([1 for num in action if num in self.past_data])
        return match_count  # 일치 개수만큼 보상 부여

    def train_q_learning(self, episodes=10000, alpha=0.1, gamma=0.9, epsilon=0.1):
        """Q-learning 알고리즘을 사용하여 학습"""
        for _ in range(episodes):
            state = self.reset()
            action = self.select_action(state, epsilon)
            
            # 인덱스 범위를 0~44로 제한
            action = [num - 1 for num in action]

            _, reward = self.step(action)

            best_next_action = np.argmax(self.q_table[action])
            
            # Q-learning 업데이트 (인덱스 범위 조정)
            self.q_table[action, best_next_action] = (
                (1 - alpha) * self.q_table[action, best_next_action] +
                alpha * (reward + gamma * np.max(self.q_table[best_next_action]))
            )

    def select_action(self, state, epsilon=0.1):
        """Epsilon-greedy 방식으로 행동 선택"""
        if np.random.rand() < epsilon:
            return random.sample(range(1, self.n_numbers + 1), self.n_select)
        return [num + 1 for num in np.argsort(self.q_table.sum(axis=1))[-self.n_select:]]

    def save_model(self, filename="q_table.pkl"):
        """학습된 Q-table 저장"""
        with open(filename, "wb") as f:
            pickle.dump(self.q_table, f)

    def load_model(self, filename="q_table.pkl"):
        """저장된 Q-table 불러오기"""
        with open(filename, "rb") as f:
            self.q_table = pickle.load(f)

# 과거 로또 당첨 번호 예제
past_winning_numbers = [3, 9, 27, 28, 38, 39, 7, 10, 16, 19, 27, 37, 38, 30, 31, 34, 39, 41, 45]

# 환경 및 학습 설정
env = LottoEnvRL(past_winning_numbers)
env.train_q_learning(episodes=5000)  # 5000번 학습 실행
env.save_model()  # 학습된 Q-table 저장

# 학습된 Q-table을 활용한 로또 번호 추천
recommended_numbers = env.select_action(env.state)
print(f"추천 로또 번호: {recommended_numbers}")
