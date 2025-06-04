import pandas as pd
import asyncio
from typing import AsyncGenerator
from loguru import logger

from fastapi import Depends

from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from sqlalchemy import Column, String, Boolean, Integer, MetaData, insert, select, or_
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from fastapi_service.config import settings


metadata = MetaData()


class Base(DeclarativeBase):
    pass


class AuthUser(SQLAlchemyBaseUserTable[int], Base):
    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(length=319), unique=True, index=True, nullable=False)
    username: str = Column(String(length=16), unique=True, index=True, nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=True)
    is_superuser: bool = Column(Boolean, default=False, nullable=True)
    is_verified: bool = Column(Boolean, default=False, nullable=True)


async_engine = create_async_engine(
    url=settings.database_url_asyncpg,
    echo=True,
)

async_session = async_sessionmaker(async_engine)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, AuthUser)


async def fill_bot_table():
    from bot_handling.models import bot

    data = pd.read_excel('bot_handling/data/bots_info.xlsx')
    df = pd.DataFrame(data, columns=['bot_name', 'bot_tagname', 'bot_link'])

    for name, link in zip(df['bot_name'], df['bot_link']):
        async with async_engine.connect() as conn:
            stmp = select(bot).where(or_(
                bot.c.bot_name == name,
                bot.c.bot_link == link
            ))
            result = await conn.execute(stmp)
            if not result.mappings().all():
                stmp = insert(bot).values(
                    [
                        {
                            'bot_name': name,
                            'bot_link': link
                        }
                    ]
                )

                await conn.execute(stmp)
                await conn.commit()
            else:
                logger.info(f"{name} and {link} - exists on database")


if __name__ == '__main__':
    asyncio.run(fill_bot_table())