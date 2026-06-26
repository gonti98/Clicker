from ..state import GameState
from .definitions import BUILDINGS


def get_income_per_unit(state: GameState, building_key: str) -> float:
    definition = BUILDINGS[building_key]
    return definition.base_income


def get_income_per_type(state: GameState, building_key: str) -> float:
    count = state.buildings[building_key].count
    return get_income_per_unit(state, building_key) * count


def get_income_total(state: GameState) -> float:
    return sum(get_income_per_type(state, key) for key in state.buildings)


def get_building_cost(state: GameState, building_key: str) -> float:
    definition = BUILDINGS[building_key]
    building_state = state.buildings[building_key]

    base_building_cost = definition.base_building_cost
    growth_rate = definition.growth_rate
    count = building_state.count

    building_cost = base_building_cost * (growth_rate**count)

    return building_cost


def get_building_income(state: GameState, building_key: str) -> float:
    definition = BUILDINGS[building_key]
    count = state.buildings[building_key].count
    return definition.base_income * count


def try_buy_building(state: GameState, building_key: str) -> bool:
    cost = get_building_cost(state, building_key)

    if state.score < cost:
        return False

    state.score -= cost
    state.buildings[building_key].count += 1
    return True
