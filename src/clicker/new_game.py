from .game_state import GameState, BuildingState
from .buildings.definitions import BUILDINGS

def new_game() -> GameState:
    return GameState(
        score=0,
        buildings={key: BuildingState() for key in BUILDINGS}
    )
