# Webzella MiniApp Bot

Простой Telegram-бот на `aiogram` 3, который при команде `/start` приветствует пользователя и предлагает открыть мини-приложение команды Webzella.

## Быстрый старт

1. Скопируй `.env` файл с `BOT_TOKEN=<токен>` или установи переменную окружения `BOT_TOKEN`.
2. Установи зависимости:
   ```bash
   poetry install
   ```
3. Запусти бота:
   ```bash
   poetry run python main.py
   ```

## Работа с Docker

Контейнер собирается из `Dockerfile`, использует `python:3.11-slim`, устанавливает зависимости через `poetry` и запускает `main.py`.

### Сборка
```bash
docker build -t webzella-miniapp-bot .
```

### Запуск
```bash
docker run --env BOT_TOKEN=<токен> webzella-miniapp-bot
```

## Мини-приложение

URL мини-приложения задаётся в `MINI_APP_URL` в `main.py`. Кнопка «🛍️ Магазин» в сообщении `/start` и под ним открывает этот URL через `WebAppInfo`.
