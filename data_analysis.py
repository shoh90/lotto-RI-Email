import numpy as np

def analyze_lotto_data(lotto_results):
    all_numbers = np.array(lotto_results).flatten()
    unique, counts = np.unique(all_numbers, return_counts=True)
    number_freq = dict(zip(unique, counts))
    
    sorted_numbers = sorted(number_freq.items(), key=lambda x: x[1], reverse=True)
    hot_numbers = [num for num, freq in sorted_numbers[:10]]  # 상위 10개 핫 넘버
    cold_numbers = [num for num, freq in sorted_numbers[-10:]]  # 하위 10개 콜드 넘버
    
    return hot_numbers, cold_numbers
