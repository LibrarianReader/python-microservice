from pydantic import BaseModel
from typing import List, Optional

class AnimeIn(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts_id: List[int]


class AnimeOut(AnimeIn):
    id: int


class AnimeUpdate(AnimeIn):
    name: Optional[str] = None
    plot: Optional[str] = None
    genres: Optional[List[str]] = None
    casts_id: Optional[List[int]] = None