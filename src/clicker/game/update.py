from .state import GameState
from .buildings.economy import get_income_total


def update_game(state: GameState, delta_time: float) -> None:
    state.played_time += delta_time
    buildings_income = get_income_total(state)
    earned = buildings_income * delta_time
    state.score += earned
