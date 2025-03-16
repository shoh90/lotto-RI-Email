from lotto import optimized_numbers
from email_service import send_email

# 추천된 로또 번호 출력 및 이메일 전송
print(f"최종 추천 로또 번호: {optimized_numbers}")
send_email(optimized_numbers)
