import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

class LottoDQN:
    def __init__(self, n_numbers=45, n_select=6, model_path="lotto_dqn.keras"):
        self.n_numbers = n_numbers
        self.n_select = n_select
        self.model_path = model_path
        self.model = self.load_model() if os.path.exists(model_path) else self.build_model()

    def build_model(self):
        model = Sequential([
            Dense(128, activation='relu', input_shape=(self.n_numbers,)),
            Dense(128, activation='relu'),
            Dense(self.n_numbers, activation='linear')
        ])
        model.compile(loss='mse', optimizer=Adam(learning_rate=0.001))
        return model

    def train(self, lotto_results, epochs=1000):
        print(f"🔍 로또 데이터 샘플: {lotto_results[:5]}")

        # 🔥 데이터 변환 (One-Hot Encoding 적용)
        X_train = np.zeros((len(lotto_results), self.n_numbers))
        for i, numbers in enumerate(lotto_results):
            for num in numbers:
                X_train[i, num - 1] = 1  # 1부터 45까지 값이므로 index 보정

        Y_train = X_train  # 타겟 값도 동일하게 설정
        print(f"✅ 변환된 X_train 샘플: {X_train[:5]}")

        self.model.fit(X_train, Y_train, epochs=epochs, verbose=1)

    def predict_numbers(self):
        state = np.zeros((1, self.n_numbers))
        q_values = self.model.predict(state)
        return np.argsort(q_values[0])[-self.n_select:]

    def save_model(self):
        """🔥 모델 저장 (GitHub Actions에서 활용)"""
        self.model.save(self.model_path)
        print("✅ 학습된 모델이 저장되었습니다!")

    def load_model(self):
        """🔥 기존 학습된 모델 불러오기 (GitHub Actions 연동)"""
        try:
            model = tf.keras.models.load_model(self.model_path)
            print("✅ 기존 학습된 모델을 성공적으로 불러왔습니다!")
            return model
        except:
            print("⚠️ 저장된 모델을 찾을 수 없습니다. 새로운 모델을 학습합니다.")
            return self.build_model()
