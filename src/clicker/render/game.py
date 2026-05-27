from .text import center_string
from ..game_state import GameState
from ..buildings.definitions import BUILDINGS


def draw_game(stdscr, current_game: GameState) -> None:
    center_string(stdscr, str(current_game.score))
    stdscr.addstr(0, 0, f"buildings: {len(current_game.buildings)}")

    row = 2
    for building_key, building_state in current_game.buildings.items():
        definition = BUILDINGS[building_key]
        building_name = definition.name
        count = building_state.count
        income = definition.base_income
        cost = definition.base_cost
        line = f"{building_name}: count={count}, income={income}, cost={cost}"

        stdscr.addstr(row, 0, line)
        row += 1
