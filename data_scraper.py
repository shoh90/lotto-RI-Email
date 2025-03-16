import requests
from bs4 import BeautifulSoup

def get_latest_draw_number():
    """ 🔥 공식 dhlottery API에서 최신 로또 회차 번호 가져오기 """
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1"  # 최신 회차 요청
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        latest_draw = data.get("drwNo")
        if isinstance(latest_draw, int) and latest_draw > 0:
            print(f"✅ 최신 회차 번호: {latest_draw}")
            return latest_draw
    print(f"❌ 오류: API에서 최신 회차 번호를 가져올 수 없음. 웹 크롤링 방식으로 전환")
    return get_latest_draw_number_scraping()

def get_latest_draw_number_scraping():
    """ 🔥 네이버 검색에서 최신 회차 번호 가져오기 (API 차단 대비) """
    url = "https://search.naver.com/search.naver?query=로또"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        latest_draw_tag = soup.select_one(".api_txt_lines")  # 네이버 검색 결과에서 최신 회차 추출
        if latest_draw_tag:
            latest_draw = int(latest_draw_tag.text.split()[1])  # "제 1163회" → 1163 추출
            print(f"✅ (웹 크롤링) 최신 회차 번호: {latest_draw}")
            return latest_draw
    print(f"❌ (웹 크롤링) 최신 회차 정보를 가져올 수 없습니다.")
    return None

def fetch_lotto_data():
    """ 🔥 최근 5회차 로또 당첨 번호 가져오기 """
    latest_draw = get_latest_draw_number()
    if latest_draw is None:
        print("❌ 최신 회차 정보를 가져올 수 없습니다.")
        return []

    base_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="
    lotto_results = []

    for i in range(latest_draw - 4, latest_draw + 1):  # 최신 5회차 데이터 가져오기
        response = requests.get(base_url + str(i))
        if response.status_code == 200:
            data = response.json()
            numbers = [
                data.get("drwtNo1"), data.get("drwtNo2"), data.get("drwtNo3"),
                data.get("drwtNo4"), data.get("drwtNo5"), data.get("drwtNo6")
            ]
            if None not in numbers and len(numbers) == 6:
                lotto_results.append(numbers)
            else:
                print(f"⚠️ 회차 {i}: 당첨 번호가 비어있거나 잘못된 데이터입니다!")
        else:
            print(f"⚠️ 회차 {i}: 데이터 가져오기 실패 (응답 코드 {response.status_code})")

    if len(lotto_results) < 5:
        print(f"❌ 충분한 로또 데이터를 가져오지 못했습니다! ({len(lotto_results)}개)")
    
    return lotto_results

# 테스트 실행
if __name__ == "__main__":
    latest_lotto_numbers = fetch_lotto_data()
    print("✅ 최신 로또 당첨 번호:", latest_lotto_numbers)
