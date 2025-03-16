from lotto import select_numbers, env, model
from email_service import send_email

# 로또 번호 추천 및 이메일 전송
recommended_numbers = select_numbers(model, env)
send_email(recommended_numbers)
