import random
from lotto_env import LottoEnv
from model import LottoDQN
from data_scraper import fetch_lotto_data
from data_analysis import analyze_lotto_data
from optimizer import optimize_lotto_numbers

# 🟢 1️⃣ 과거 로또 데이터 가져오기
lotto_results = fetch_lotto_data()

if not lotto_results or len(lotto_results) < 5:
    print("⚠️ 최신 로또 데이터를 충분히 가져오지 못했습니다. 기본 데이터로 진행합니다.")
    lotto_results = [
        [2, 13, 15, 16, 33, 43],
        [20, 21, 22, 25, 28, 29],
        [2, 12, 20, 24, 34, 42],
        [7, 13, 18, 36, 39, 45],
        [3, 9, 27, 28, 38, 39]
    ]  # 🔥 기본 데이터 (백업)

print(f"✅ 최신 5개 회차 로또 데이터: {lotto_results}")

# 🟢 2️⃣ 데이터 분석 (핫 넘버 & 콜드 넘버)
hot_numbers, cold_numbers = analyze_lotto_data(lotto_results)
print(f"🔥 핫 넘버: {hot_numbers}, ❄️ 콜드 넘버: {cold_numbers}")

# 🟢 3️⃣ DQN 모델 생성 및 학습
lotto_dqn = LottoDQN()
lotto_dqn.train(lotto_results)

# 🟢 4️⃣ DQN을 활용한 로또 번호 예측
predicted_numbers = lotto_dqn.predict_numbers()
print(f"🤖 DQN 모델 예측 번호: {predicted_numbers}")

# 🟢 5️⃣ 번호 조합 최적화
optimized_numbers = optimize_lotto_numbers(predicted_numbers, hot_numbers, cold_numbers)

# 🔥 중복 제거 및 오름차순 정렬 추가
optimized_numbers = sorted(set(optimized_numbers))

# 🔥 중복이 제거된 후 숫자가 6개가 안 되면 추가 보완 (핫 넘버 우선 추가)
while len(optimized_numbers) < 6:
    potential_numbers = list(set(range(1, 46)) - set(optimized_numbers))  # 사용 가능한 숫자 리스트
    extra_number = random.choice(hot_numbers) if hot_numbers else random.choice(potential_numbers)  # 핫 넘버 우선 추가
    if extra_number not in optimized_numbers:
        optimized_numbers.append(extra_number)

optimized_numbers = sorted(optimized_numbers)  # 다시 정렬

print(f"✅ 최종 추천 로또 번호: {optimized_numbers}")

# 모델 저장
lotto_dqn.save_model()
