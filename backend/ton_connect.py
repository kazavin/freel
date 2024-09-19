import requests
from config import TON_API_URL, TON_API_TOKEN

class TonConnect:
    def __init__(self):
        self.api_url = TON_API_URL
        self.headers = {
            'Authorization': f'Bearer {TON_API_TOKEN}'
        }

    def perform_transaction(self, wallet_address):
        # Выполняем запрос на выполнение транзакции через TON API
        try:
            response = requests.post(
                f"{self.api_url}/transactions/send", 
                headers=self.headers, 
                json={
                    "from": wallet_address,
                    "to": "адрес получателя",  # Укажите адрес получателя
                    "amount": 1000000  # Укажите сумму в нанотоннах (например, 1,000,000 = 0.001 TON)
                }
            )
            if response.status_code == 200:
                # Если запрос успешен, возвращаем хэш транзакции
                transaction_data = response.json()
                return transaction_data['transactionHash']
            else:
                return None
        except requests.RequestException:
            return None
