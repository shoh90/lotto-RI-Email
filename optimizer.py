import random

def optimize_lotto_numbers(predicted_numbers, hot_numbers, cold_numbers):
    """ 🔥 로또 번호 최적화 (핫 넘버 반영) """
    optimized = sorted(set(predicted_numbers))  # 중복 제거 및 정렬
    print(f"🎯 초기 예측 번호: {optimized}")

    # 🔥 최적화 과정
    for num in cold_numbers:
        if num in optimized:
            optimized.remove(num)  # ❄️ 콜드 넘버 제거
            print(f"❌ 콜드 넘버 {num} 제거!")

    # 🔥 부족한 개수를 핫 넘버 또는 랜덤으로 채움
    while len(optimized) < 6:
        new_number = random.choice(hot_numbers) if hot_numbers else random.randint(1, 45)
        if new_number not in optimized:
            optimized.append(new_number)
            print(f"➕ 핫 넘버 {new_number} 추가!")

    optimized = sorted(optimized)
    print(f"✅ 최적화된 추천 번호: {optimized}")
    return optimized
