from ..state import GameState
from .definitions import BUILDINGS


def get_building_cost(state: GameState, building_key: str) -> int:
    definition = BUILDINGS[building_key]
    building_state = state.buildings[building_key]

    base_building_cost = definition.base_building_cost
    growth_rate = definition.growth_rate
    count = building_state.count

    building_cost = base_building_cost * (growth_rate ** count)

    return int(building_cost)

def get_building_income(state: GameState, building_key: str) -> int:
    definition = BUILDINGS[building_key]
    count = state.buildings[building_key].count
    return int(definition.base_income * count)

def try_buy_building(state: GameState, building_key: str) -> bool:
    cost = get_building_cost(state, building_key)

    if state.score < cost:
        return False

    state.score -= cost
    state.buildings[building_key].count += 1
    return True
