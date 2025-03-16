가져오기 요청
무작위 가져오기

def fetch_lotto_data ():
 URL = "https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo="
 로또_results = []
    
 for i in range(900, 1159): # 최근 900회차부터 최신 1159회차까지 스크래핑
 응답 = requests.get(url + str(i))
 if response.status_code == 200:
 숫자 = parse_lotto_numbers(response.text)
 lotto_results.append(numbers)
    
 반품 로또_results

def parse_lotto_numbers(html_text):
 반환 [random.randint(1, 45) for _ in range(6)] # 예제용 랜덤 데이터 (실제 HTML 파싱 필요)
