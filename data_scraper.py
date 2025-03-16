import requests

def get_latest_draw_number():
    """ 🔥 신뢰할 수 있는 API를 활용하여 최신 로또 회차 번호 가져오기 """
    url = "https://dhlottery.roeniss.xyz/v1/last"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        latest_draw = data.get("drwNo")
        if isinstance(latest_draw, int) and latest_draw > 0:
            print(f"✅ 최신 회차 번호: {latest_draw}")
            return latest_draw
        else:
            print(f"❌ 오류: API에서 잘못된 최신 회차 값({latest_draw})을 반환함!")
            return None
    else:
        print(f"❌ 최신 회차 정보를 가져오는 데 실패했습니다. (응답 코드: {response.status_code})")
        return None

def fetch_lotto_data():
    """ 🔥 최근 5회차 로또 당첨 번호 가져오기 """
    latest_draw = get_latest_draw_number()
    if latest_draw is None:
        print("❌ 최신 회차 정보를 가져올 수 없습니다.")
        return []

    base_url = "https://dhlottery.roeniss.xyz/v1/"
    lotto_results = []

    for i in range(latest_draw - 4, latest_draw + 1):  # 최신 5회차 데이터 가져오기
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
                print(f"⚠️ 회차 {i}: 당첨 번호가 비어있거나 잘못된 데이터입니다! API 응답 확인 필요!")
        else:
            print(f"⚠️ 회차 {i}: 데이터 가져오기 실패 (응답 코드 {response.status_code})")

    if len(lotto_results) < 5:
        print(f"❌ 충분한 로또 데이터를 가져오지 못했습니다! ({len(lotto_results)}개)")
    
    return lotto_results

# 테스트 실행
if __name__ == "__main__":
    latest_lotto_numbers = fetch_lotto_data()
    print("✅ 최신 로또 당첨 번호:", latest_lotto_numbers)
