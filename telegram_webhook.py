import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_API_URL

def set_webhook():
    url = f'{TELEGRAM_API_URL}/bot{TELEGRAM_BOT_TOKEN}/setWebhook'
    webhook_url = 'https://ваш_сервер/webhook/ваш_секретный_URL_для_вебхуков'
    payload = {'url': webhook_url}
    requests.post(url, json=payload)

if __name__ == '__main__':
    set_webhook()
