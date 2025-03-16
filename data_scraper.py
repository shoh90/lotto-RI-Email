import requests
import random
import time

def fetch_lotto_data():
    url = "https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo="
    lotto_results = []
    
    for i in range(900, 1159):  # 최근 900회차부터 최신 1159회차까지 스크래핑
        attempt = 0
        success = False

        while attempt < 3 and not success:  # 최대 3번 재시도
            try:
                response = requests.get(url + str(i), timeout=5)
                if response.status_code == 200:
                    numbers = parse_lotto_numbers(response.text)
                    lotto_results.append(numbers)
                    success = True
                else:
                    print(f"⚠️ 회차 {i}: 서버 응답 코드 {response.status_code}, 재시도 중...")
            except requests.exceptions.RequestException as e:
                print(f"⚠️ 회차 {i}: 연결 오류 발생 - {e}, 재시도 중...")
            
            attempt += 1
            time.sleep(2)  # 2초 대기 후 재시도

    return lotto_results

def parse_lotto_numbers(html_text):
    return [random.randint(1, 45) for _ in range(6)]  # 예제용 랜덤 데이터 (실제 HTML 파싱 필요)
