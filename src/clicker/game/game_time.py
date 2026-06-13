import time
from .game_state import GameState


def time_elapsed(current_game: GameState) -> float:
    return float(time.monotonic() - current_game.started_at)
