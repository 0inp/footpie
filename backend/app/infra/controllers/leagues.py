from typing import Any
from fastapi import APIRouter

from app.domain.usecases.leagues_usecase import LeaguesListUsecase


router = APIRouter()


@router.get("/leagues/")
async def get_leagues() -> list[Any]:
    usecase = LeaguesListUsecase()
    leagues = usecase.execute()
    return leagues
