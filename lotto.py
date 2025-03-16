```python
import random
import numpy as np
from lotto_env import LottoEnv
from model import build_model

# 로또 데이터 예제 (이전 당첨 번호 저장)
past_winning_numbers = [3, 9, 27, 28, 38, 39, 7, 10, 16, 19, 27, 37, 38, 30, 31, 34, 39, 41, 45]

# 환경 및 모델 설정
env = LottoEnv(past_winning_numbers)
state_dim = env.n_numbers
model = build_model(state_dim)

# 로또 번호 추천 함수
def select_numbers(model, env, epsilon=0.1):
    state = env.reset().reshape(1, -1)
    if np.random.rand() < epsilon:
        return random.sample(range(1, env.n_numbers + 1), env.n_select)
    
    try:
        q_values = model.predict(state)
        return np.argsort(q_values[0])[-env.n_select:]
    except Exception:
        return random.sample(range(1, env.n_numbers + 1), env.n_select)  # 모델이 초기화되지 않았을 경우 랜덤값 반환

# 로또 번호 추천 및 출력
recommended_numbers = select_numbers(model, env)
print(f"추천 로또 번호: {recommended_numbers}")
```