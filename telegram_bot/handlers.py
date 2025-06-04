from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    username = f"{message.from_user.full_name}"
    await message.answer(
        f'''Привет, {username}! Вы можете отправить мне любое сообщение, а я пришлю вам количество его символов. Начнем?'''
    )


@router.message()
async def send_count_characters(message: Message):
    count = len(message.text)
    await message.answer(f"Вы отправили сообщение длиной {count} символов")