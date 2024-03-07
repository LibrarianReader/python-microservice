from app.api.models import AnimeIn, AnimeOut, AnimeUpdate
from app.api.db import animes, database


async def add_anime(payload: AnimeIn):
    query = animes.insert().values(**payload.dict())

    return await database.execute(query=query)

async def get_all_animes():
    query = animes.select()
    return await database.fetch_all(query=query)

async def get_anime(id):
    query = animes.select(animes.c.id==id)
    return await database.fetch_one(query=query)

async def delete_anime(id: int):
    query = animes.delete().where(animes.c.id==id)
    return await database.execute(query=query)

async def update_anime(id: int, payload: AnimeIn):
    query = (
        animes
        .update()
        .where(animes.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)