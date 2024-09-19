from flask import Flask, render_template, request, jsonify
import requests
from ton_connect import TonConnect
from config import TELEGRAM_BOT_URL

app = Flask(__name__)

# Инициализация TON Connect
ton_connect = TonConnect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connect_wallet', methods=['POST'])
def connect_wallet():
    # Получаем адрес кошелька от клиента
    wallet_address = request.json.get('wallet_address')
    
    # Выполняем транзакцию через TON Connect
    transaction_hash = ton_connect.perform_transaction(wallet_address)
    
    if transaction_hash:
        # Формируем ссылку на просмотр транзакции на TON Explorer (например, на tonscan.org)
        transaction_link = f"https://tonscan.org/tx/{transaction_hash}"
        return jsonify({'status': 'success', 'message': 'Транзакция успешно выполнена!', 'link': transaction_link})
    else:
        return jsonify({'status': 'error', 'message': 'Ошибка выполнения транзакции. Попробуйте снова.'})

# Обработка вебхуков от Telegram
@app.route(f'/webhook/{TELEGRAM_BOT_URL}', methods=['POST'])
def telegram_webhook():
    from telegram_bot import process_telegram_message
    message = request.json
    process_telegram_message(message)
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)
