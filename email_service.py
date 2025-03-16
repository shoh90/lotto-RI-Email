```python
import smtplib
import os
from email.mime.text import MIMEText

# 이메일 전송 함수
def send_email(recommended_numbers):
    sender_email = os.getenv('EMAIL_SENDER')  # GitHub Secrets에서 불러옴
    sender_password = os.getenv('EMAIL_PASSWORD')
    recipient_email = os.getenv('EMAIL_RECIPIENT')
    
    subject = "로또 추천 번호 알림"
    body = f"이번 주 추천 로또 번호: {recommended_numbers}"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    try:
        with smtplib.SMTP_SSL('smtp.naver.com', 465) as server:  # 네이버 메일 사용 시
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("이메일 전송 완료!")
    except Exception as e:
        print(f"이메일 전송 실패: {e}")
```