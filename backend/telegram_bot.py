import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_API_URL

def send_message(chat_id, text):
    url = f'{TELEGRAM_API_URL}/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, json=payload)

def process_telegram_message(message):
    chat_id = message['message']['chat']['id']
    text = message['message']['text']
    
    # Логика обработки сообщений
    if text == '/start':
        send_message(chat_id, 'Добро пожаловать на нашу фриланс биржу! Вы можете подключить TON кошелек для оплаты.')
    elif text == '/connect':
        send_message(chat_id, 'Пожалуйста, откройте Mini App для подключения кошелька.')
    else:
        send_message(chat_id, 'Команда не распознана. Попробуйте снова.')
