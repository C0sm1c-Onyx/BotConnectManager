# BotConnectManager

## Инструкция по развертыванию сервиса
### Установка и настройка окружения
1. Склонируйте репозиторий
```bash
git clone https://github.com/C0sm1c-Onyx/BotConnectManager.git
```
2. Отредактируйте три переменные окружения под свои (если надо)
```env
POSTGRES_USER='postgres'
POSTGRES_PASSWORD='postgres'
POSTGRES_DB_NAME='postgres'
```
### Запуск проекта
```bash
cd BotConnectManager
```
```bash
docker-compose up --build
```
## API:

### 1. Регистрация - POST http://127.0.0.1:8000/auth/register
Пример входных данных:
```bash
{
    "email": "root@gmail.com",
    "username": "root",
    "password": "root_toor"
}
```
### 2. Авторизация - POST http://127.0.0.1:8000/auth/login
Пример входных данных:
```bash
{
    "username": "root@gmail.com",
    "password": "root_toor"
}
```
![alt text](https://www.flickr.com/photos/202946803@N04/54568272865/)
### 3. Просмотр всех ботов - GET http://127.0.0.1:8000/bot/bot-list/

### 4. Подключить бота - POST http://127.0.0.1:8000/bot/connect-bot/
Пример входных данных:
```bash
{
    "bot_id": 1
}
```

### 5. Просмотр подключенных ботов - GET http://127.0.0.1:8000/bot/my_connected_bot/

## Telegram bot
### ссылка на телеграмм бота: https://t.me/sender_character_count_bot   
