from fastapi import APIRouter, Depends
from sqlalchemy import insert, select, join, and_

from auth.auth import get_current_user
from database import async_engine
from bot_handling.models import connected_user_bot, bot
from fastapi_service.database import async_session
from fastapi_service.utils import exists_in_db


router = APIRouter()


@router.get("/bot-list/")
async def get_all_bots():
    async with async_engine.connect() as conn:
        stmp = select(bot)
        data = await conn.execute(stmp)

        return {"bots": data.mappings().all()}


@router.post("/connect-bot/")
async def connect_bot_user(data: dict, current_user = Depends(get_current_user)):
    bot_id = data.get('bot_id')

    async with async_engine.connect() as conn:
        if not exists_in_db(async_session, connected_user_bot, user_id=current_user, bot_id=bot_id):
            stmp = insert(connected_user_bot).values(
                [
                    {
                        'user_id': current_user,
                        'bot_id': bot_id
                    }
                ]
            )
            try:
                await conn.execute(stmp)
                await conn.commit()
            except Exception as error:
                return {"error": f"A bot with id {bot_id} doesn't exist"}
        else:
            return {"message": "you've already added"}


    return {"message": "Success!"}


@router.get('/my_connected_bot/')
async def get_connected_bot_user(current_user = Depends(get_current_user)):
    async with async_engine.connect() as conn:
        stmp = select(
            connected_user_bot.c.bot_id,
            bot.c.bot_name,
            bot.c.bot_link
        ).select_from(
            join(connected_user_bot, bot, connected_user_bot.c.bot_id == bot.c.id)
        ).where(connected_user_bot.c.user_id == current_user)

        data = await conn.execute(stmp)

        return {'my_bots': data.mappings().all()}