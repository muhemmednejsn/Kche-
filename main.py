import requests
import os
import time

BOT_TOKEN = os.getenv('TELEGRAM BOTTOKEN')
CHAT_ID = os.getenv('TELEGRAM_ID')
MESSAGE_TEXT = 'kche bykawa amozatm tawaww basha ble awa manera naynerm'


def send_message(text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': text,
        'disable_notification': True  # Silent message
    }
    response = requests.post(url, data=payload)
    return response.json()

# Simple for-loop sending messages
i = 1
while i == i:
    send_message(msg)
    time.sleep(3)  # Delay between messages
