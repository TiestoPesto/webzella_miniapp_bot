import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from dotenv import load_dotenv
import os

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

# URL вашего мини-приложения (из BotFather)
MINI_APP_URL = "https://tg-miniapp.webzella.ru/"  # Замените на реальный URL


# Создаем клавиатуру с кнопкой для мини-приложения
def get_main_keyboard():
    # Создаем инлайн кнопку для мини-приложения
    web_app_button = InlineKeyboardButton(
        text="🛍️ Магазин",
        web_app=WebAppInfo(url=MINI_APP_URL)
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[web_app_button]]
    )
    return keyboard


# Обработчик команды /start
@dp.message(CommandStart())
async def cmd_start(message: Message):
    welcome_text = (
        "👋 Привет! Это бот мини-приложения команды Webzella.ru.\n\n"
        "Для открытия мини-приложения нажмите на кнопку 'Магазин' ниже 👇\n\n"
        "Кнопка под сообщением ведёт прямо в миниап."
    )

    await message.answer(
        text=welcome_text,
        reply_markup=get_main_keyboard()
    )


# Обработчик текстовых сообщений (если пользователь просто пишет "магазин")
@dp.message(F.text.lower().in_(["магазин", "shop", "меню"]))
async def handle_shop_text(message: Message):
    await message.answer(
        text="Открываю магазин... 🛍️",
        reply_markup=get_main_keyboard()
    )


# Обработчик обратного вызова от инлайн кнопок (если понадобится в будущем)
@dp.callback_query(F.data == "open_miniapp")
async def handle_miniapp_callback(callback_query):
    await callback_query.answer()
    await callback_query.message.answer(
        text="Открываю мини-приложение...",
        reply_markup=get_main_keyboard()
    )


# Основная функция запуска бота
async def main():
    logging.info("Запуск бота...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Бот остановлен вручную.")