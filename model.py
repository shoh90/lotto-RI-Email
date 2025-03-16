import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

class LottoDQN:
    def __init__(self, n_numbers=45, n_select=6):
        self.n_numbers = n_numbers
        self.n_select = n_select
        self.model = self.build_model()
    
    def build_model(self):
        model = Sequential([
            Dense(128, activation='relu', input_shape=(self.n_numbers,)),
            Dense(128, activation='relu'),
            Dense(self.n_numbers, activation='linear')
        ])
        model.compile(loss='mse', optimizer=Adam(learning_rate=0.001))
        return model
    
    def train(self, lotto_results, epochs=1000):
        """🔥 One-Hot Encoding을 적용하여 데이터 변환"""
        print(f"🔍 로또 데이터 샘플: {lotto_results[:5]}")  # 데이터 확인

        # 🔥 데이터 필터링: 리스트 형태이며 6개 숫자가 있는 경우만 포함
        lotto_results = [numbers for numbers in lotto_results if isinstance(numbers, list) and len(numbers) == 6]

        if not lotto_results:  
            raise ValueError("⚠️ 유효한 로또 데이터가 없습니다. 데이터 스크래핑을 확인하세요!")

        # 🔥 one-hot encoding 적용하여 변환 (bincount 대신)
        X_train = np.zeros((len(lotto_results), self.n_numbers))  # (샘플 수, 45)
        for i, numbers in enumerate(lotto_results):
            for num in numbers:
                X_train[i, num - 1] = 1  # 1부터 45까지 값이므로 index 보정

        Y_train = X_train  # 타겟 값도 동일하게 설정

        # 🔥 데이터 형식 확인
        print(f"✅ 변환된 X_train 샘플: {X_train[:5]}")

        self.model.fit(X_train, Y_train, epochs=epochs, verbose=1)
    
    def predict_numbers(self):
        state = np.zeros((1, self.n_numbers))
        q_values = self.model.predict(state)
        return np.argsort(q_values[0])[-self.n_select:]
    
    def save_model(self, filename="lotto_dqn.keras"):
        self.model.save(filename)  # 🔥 모델 저장

    def load_model(self, filename="lotto_dqn.keras"):
        try:
        self.model = tf.keras.models.load_model(filename)  # 🔥 모델 로드
        print("✅ 학습된 모델을 성공적으로 불러왔습니다!")
    except:
        print("⚠️ 저장된 모델을 찾을 수 없습니다. 새로운 모델을 학습합니다.")
        self.model = self.build_model()  # 모델 새로 생성
