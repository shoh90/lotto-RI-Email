로또_env 가져오기 로또Env에서
모델 가져오기 로또DQN에서
from data_scraper 가져오기_lotto_data
from data_analysis 가져오기 분석_lotto_data
옵티마이저에서 가져오기 optimize_lotto_numbers

# 🟢 1️⃣ 과거 로또 데이터 가져오기
로또_results = fetch_lotto_data ()

# 🟢 2️⃣ 데이터 분석 (핫 넘버 & 콜드 넘버)
핫_numbers, 콜드_numbers = 분석_lotto_데이터(lotto_results)

# 🟢 3️⃣ DQN 모델 생성 및 학습
lotto_dqn = LottoDQN()
로또_dqn.train(lotto_results)

# 🟢 4️⃣ DQN을 활용한 로또 번호 예측
예측_numbers =로또_dqn.predict_numbers()

# 🟢 5️⃣ 번호 조합 최적화
optimized_numbers = optimize_lotto_numbers(predicted_numbers, hot_numbers, cold_numbers)

인쇄(f"추천 로또 번호: {optimized_numbers}")

# 모델 저장
로또_dqn.save_model ()
