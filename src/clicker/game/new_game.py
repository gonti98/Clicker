import time

from .state import GameState, BuildingState, ManualClickState
from .buildings.definitions import BUILDINGS


def new_game() -> GameState:
    now = time.monotonic()

    return GameState(
        score=0.0,
        buildings={key: BuildingState() for key in BUILDINGS},
        manual_click=ManualClickState(ready_at=now),
    )
