import random

def optimize_lotto_numbers(predicted_numbers, hot_numbers, cold_numbers):
    optimized = []
    
    # 홀수 3개 + 짝수 3개 유지
    odd_numbers = [num for num in predicted_numbers if num % 2 == 1]
    even_numbers = [num for num in predicted_numbers if num % 2 == 0]
    
    while len(odd_numbers) < 3:
        odd_numbers.append(random.choice(hot_numbers))
    while len(even_numbers) < 3:
        even_numbers.append(random.choice(cold_numbers))
    
    optimized = odd_numbers[:3] + even_numbers[:3]
    return optimized
