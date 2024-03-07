from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import AnimeOut, AnimeIn, AnimeUpdate
from app.api import db_manager
from app.api.service import is_cast_present

animes = APIRouter()

@animes.post('/', response_model=AnimeOut, status_code=201) #localhost:8001/api/v1/animes
async def create_anime(payload: AnimeIn):
    for cast_id in payload.casts_id:
        if not is_cast_present(cast_id):
            raise HTTPException(status_code=404, detail=f"Cast with given id:{cast_id} not found")

    anime_id = await db_manager.add_anime(payload)
    response = {
        'id': anime_id,
        **payload.dict()
    }

    return response

@animes.get('/', response_model=List[AnimeOut]) #localhost:8001/api/v1/animes
async def get_animes():
    return await db_manager.get_all_animes()

@animes.get('/{id}/', response_model=AnimeOut) #localhost:8001/api/v1/animes/1 
async def get_anime(id: int):
    anime = await db_manager.get_anime(id)
    if not anime:
        raise HTTPException(status_code=404, detail="Anime not found")
    return anime

@animes.put('/{id}/', response_model=AnimeOut) #localhost:8001/api/v1/animes/1 - Обновит страницу
async def update_anime(id: int, payload: AnimeUpdate):
    anime = await db_manager.get_anime(id)
    if not anime:
        raise HTTPException(status_code=404, detail="Anime not found")

    update_data = payload.dict(exclude_unset=True)

    if 'casts_id' in update_data:
        for cast_id in payload.casts_id:
            if not is_cast_present(cast_id):
                raise HTTPException(status_code=404, detail=f"Cast with given id:{cast_id} not found")

    anime_in_db = AnimeIn(**anime)

    updated_anime = anime_in_db.copy(update=update_data)

    return await db_manager.update_anime(id, updated_anime)

@animes.delete('/{id}/', response_model=None) #localhost:8001/api/v1/animes/1 - Удалит страницу
async def delete_anime(id: int):
    anime = await db_manager.get_anime(id)
    if not anime:
        raise HTTPException(status_code=404, detail="Anime not found")
    return await db_manager.delete_anime(id)