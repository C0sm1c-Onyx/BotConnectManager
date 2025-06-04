from sqlalchemy import Table, Column, Integer, ForeignKey, String

from fastapi_service.database import metadata
from fastapi_service.auth.models import user


bot = Table(
    'bot',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('bot_name', String, nullable=False, unique=True),
    Column('bot_link', String, nullable=False, unique=True)
)


connected_user_bot = Table(
    "connected_user_bot",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('bot_id', Integer, ForeignKey('bot.id'))
)