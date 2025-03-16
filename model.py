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
        X_train = np.array([np.bincount(numbers, minlength=self.n_numbers) for numbers in lotto_results])
        Y_train = X_train  # DQN을 위한 타겟 값 설정 (당첨 패턴 학습)
        
        self.model.fit(X_train, Y_train, epochs=epochs, verbose=1)
    
    def predict_numbers(self):
        state = np.zeros((1, self.n_numbers))
        q_values = self.model.predict(state)
        return np.argsort(q_values[0])[-self.n_select:]
    
    def save_model(self, filename="lotto_dqn.h5"):
        self.model.save(filename)
    
    def load_model(self, filename="lotto_dqn.h5"):
        self.model = tf.keras.models.load_model(filename)
