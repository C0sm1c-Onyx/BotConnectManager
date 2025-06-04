from sqlalchemy.orm import Session


async def exists_in_db(async_session: Session, model, **filters):
    async with async_session as db:
        return db.query(model).filter_by(**filters).first() is not None