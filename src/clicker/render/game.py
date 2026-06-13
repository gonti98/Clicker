from .text import center_string, center_string_offset
from ..game.game_state import GameState
from ..game.game_time import time_elapsed
from ..game.buildings.definitions import BUILDINGS
from ..game.buildings.economy import get_building_cost, get_building_income


def draw_game(stdscr, current_game: GameState) -> None:
    elapsed = time_elapsed(current_game)
    stdscr.addstr(0, 0, f"time: {float(elapsed):.1f}")
    stdscr.addstr(1, 0, f"buildings: {len(current_game.buildings)}")

    offset = 2
    for building_key, building_state in current_game.buildings.items():
        definition = BUILDINGS[building_key]
        building_name = definition.name
        count = building_state.count
        income = get_building_income(current_game, building_key)
        cost = get_building_cost(current_game, building_key)
        line = f"{building_name}: count={count}, income={income}, cost={cost:.3g}"

        center_string_offset(stdscr, line, offset, 0)
        offset += 1

    center_string(stdscr, f"{current_game.score:.3g}")
