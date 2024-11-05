from abc import ABC
from dataclasses import dataclass
from typing import Any


@dataclass
class LeaguesListUsecase(ABC):
    # repo: BaseRepository

    def execute(self) -> list[Any]:
        return ["toto"]
