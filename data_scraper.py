import requests

def fetch_lotto_data():
    base_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="
    latest_draw = 1159  # 최신 회차 번호 (업데이트 필요)
    lotto_results = []

    for i in range(latest_draw - 5, latest_draw + 1):  # 최근 5회차 데이터 가져오기
        response = requests.get(base_url + str(i))
        if response.status_code == 200:
            data = response.json()
            numbers = [
                data["drwtNo1"], data["drwtNo2"], data["drwtNo3"],
                data["drwtNo4"], data["drwtNo5"], data["drwtNo6"]
            ]
            if len(numbers) == 6:  # 🔥 빈 값 방지 (정확히 6개 숫자가 있는 경우만 추가)
                lotto_results.append(numbers)
        else:
            print(f"⚠️ 회차 {i}: 데이터 가져오기 실패 (응답 코드 {response.status_code})")

    return lotto_results
