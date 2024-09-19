document.getElementById('connect-btn').addEventListener('click', function () {
    // Получаем адрес кошелька от пользователя
    let walletAddress = prompt("Введите ваш адрес TON кошелька:");

    // Отправляем запрос на сервер для подключения кошелька и выполнения транзакции
    fetch('/connect_wallet', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ wallet_address: walletAddress }),
    })
    .then(response => response.json())
    .then(data => {
        let alertDiv = document.getElementById('alert');
        if (data.status === 'success') {
            // Если транзакция успешна, выводим сообщение и ссылку на транзакцию
            alertDiv.innerHTML = `<div class="alert alert-success">${data.message} <a href="${data.link}" target="_blank">Просмотреть транзакцию</a></div>`;
        } else {
            // Если ошибка, выводим сообщение об ошибке
            alertDiv.innerHTML = `<div class="alert alert-error">${data.message}</div>`;
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
