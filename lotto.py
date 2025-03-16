from lotto_env import LottoEnv
from model import LottoDQN
from data_scraper import fetch_lotto_data
from data_analysis import analyze_lotto_data
from optimizer import optimize_lotto_numbers

# 🟢 1️⃣ 과거 로또 데이터 가져오기
lotto_results = fetch_lotto_data()

# 🟢 2️⃣ 데이터 분석 (핫 넘버 & 콜드 넘버)
hot_numbers, cold_numbers = analyze_lotto_data(lotto_results)

# 🟢 3️⃣ DQN 모델 생성 및 학습
lotto_dqn = LottoDQN()  # ✅ 객체 생성
lotto_dqn.train(lotto_results)  # ✅ train() 호출

# 🟢 4️⃣ DQN을 활용한 로또 번호 예측
predicted_numbers = lotto_dqn.predict_numbers()

# 🟢 5️⃣ 번호 조합 최적화
optimized_numbers = optimize_lotto_numbers(predicted_numbers, hot_numbers, cold_numbers)

print(f"추천 로또 번호: {optimized_numbers}")

# 모델 저장
lotto_dqn.save_model()
