from .game_state import GameState

def new_game() -> GameState:
    return GameState(score=0)
