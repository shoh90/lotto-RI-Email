import requests

def get_latest_draw_number():
    """ 🔥 로또 최신 회차 번호를 자동으로 가져오기 """
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1"  # 임시 회차 요청
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get("drwNo")  # 최신 회차 번호 반환
    else:
        print(f"⚠️ 최신 회차 정보를 가져오는 데 실패했습니다. (응답 코드: {response.status_code})")
        return None

def fetch_lotto_data():
    """ 🔥 최근 5주간 로또 당첨 번호 가져오기 """
    latest_draw = get_latest_draw_number()
    if latest_draw is None:
        print("❌ 최신 회차 정보를 가져올 수 없습니다.")
        return []

    base_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="
    lotto_results = []

    for i in range(latest_draw - 4, latest_draw + 1):  # 최근 5회차 데이터 가져오기
        response = requests.get(base_url + str(i))
        if response.status_code == 200:
            data = response.json()
            numbers = [
                data.get("drwtNo1"), data.get("drwtNo2"), data.get("drwtNo3"),
                data.get("drwtNo4"), data.get("drwtNo5"), data.get("drwtNo6")
            ]
            if None not in numbers and len(numbers) == 6:  # 🔥 빈 값 방지 (정확히 6개 숫자가 있는 경우만 추가)
                lotto_results.append(numbers)
            else:
                print(f"⚠️ 회차 {i}: 당첨 번호가 비어있습니다. API 응답 확인 필요!")
        else:
            print(f"⚠️ 회차 {i}: 데이터 가져오기 실패 (응답 코드 {response.status_code})")

    if len(lotto_results) < 5:
        print(f"❌ 충분한 로또 데이터를 가져오지 못했습니다! ({len(lotto_results)}개)")
    
    return lotto_results

# 테스트 실행
if __name__ == "__main__":
    latest_lotto_numbers = fetch_lotto_data()
    print("✅ 최신 로또 당첨 번호:", latest_lotto_numbers)
