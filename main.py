import requests
import os
import time

BOT_TOKEN = os.getenv('TELEGRAM BOTTOKEN')
CHAT_ID = os.getenv('TELEGRAM_ID')
msg = 'اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كَمَا صَلَّيْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ، اللَّهُمَّ بَارِكْ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كَمَا بَارَكْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ، إِنَّكَ حَمِيدٌ مَجِيدٌ،،/n \n kche bykawa amozatm tawaww basha ble awa manera naynerm tawaww mashykawa chonka meshk taxam saayakawka.'


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
