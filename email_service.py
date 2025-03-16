import smtplib
import os
from email.mime.text import MIMEText

# 이메일 전송 함수
def send_email(recommended_numbers):
    sender_email = os.getenv('EMAIL_SENDER')  # GitHub Secrets에서 불러옴
    sender_password = os.getenv('EMAIL_PASSWORD')
    recipient_email = os.getenv('EMAIL_RECIPIENT')

    if not sender_email or not sender_password or not recipient_email:
        print("⚠️ 이메일 환경 변수가 설정되지 않았습니다. GitHub Secrets를 확인하세요.")
        return

    subject = "로또 추천 번호 알림"
    body = f"이번 주 추천 로또 번호: {', '.join(map(str, recommended_numbers))}"

    msg = MIMEText(body, "plain", "utf-8")  # 인코딩 설정
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    try:
        with smtplib.SMTP_SSL('smtp.naver.com', 465) as server:  # 네이버 메일 사용
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string().encode("utf-8"))  # 바이트 변환 제거
        print("✅ 이메일 전송 완료!")
    except Exception as e:
        print(f"❌ 이메일 전송 실패: {e}")
