import requests
import random

def fetch_lotto_data():
    url = "https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo="
    lotto_results = []
    
    for i in range(900, 1159):  # 최근 900회차부터 최신 1159회차까지 스크래핑
        response = requests.get(url + str(i))
        if response.status_code == 200:
            numbers = parse_lotto_numbers(response.text)
            lotto_results.append(numbers)
    
    return lotto_results

def parse_lotto_numbers(html_text):
    return [random.randint(1, 45) for _ in range(6)]  # 예제용 랜덤 데이터 (실제 HTML 파싱 필요)
