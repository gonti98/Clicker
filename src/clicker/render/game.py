from .text import center_string
from ..game_state import GameState
from ..buildings.definitions import BUILDINGS
from ..buildings.economy import get_building_cost, get_building_income


def draw_game(stdscr, current_game: GameState) -> None:
    center_string(stdscr, str(current_game.score))
    stdscr.addstr(0, 0, f"buildings: {len(current_game.buildings)}")

    row = 2
    for building_key, building_state in current_game.buildings.items():
        definition = BUILDINGS[building_key]
        building_name = definition.name
        count = building_state.count
        income = get_building_income(current_game, building_key)
        cost = get_building_cost(current_game, building_key)
        line = f"{building_name}: count={count}, income={income}, cost={cost}"

        stdscr.addstr(row, 0, line)
        row += 1
