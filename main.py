from lotto import select_numbers, env
from email_service import send_email

# 로또 번호 추천 및 이메일 전송
recommended_numbers = select_numbers(env)
print(f"추천 로또 번호: {recommended_numbers}")

send_email(recommended_numbers)
