import time

from ..state import GameState
from .definitions import MANUAL_CLICK


def get_current_income(state: GameState) -> int:
    base_income = MANUAL_CLICK.base_income
    income_upgrade = state.manual_click.income_upgrade_level
    increment = MANUAL_CLICK.income_increment_per_level

    return base_income + income_upgrade * increment


def get_next_income_upgrade_cost(state: GameState) -> int:
    base_cost = MANUAL_CLICK.base_income_upgrade_cost
    income_upgrade = state.manual_click.income_upgrade_level
    growth_rate = MANUAL_CLICK.growth_rate

    upgrade_cost = base_cost * (growth_rate ** income_upgrade)

    return int(upgrade_cost)


def try_manual_click(state: GameState) -> bool:
    now = time.monotonic()

    if now < state.manual_click.ready_at:
        return False

    state.score += get_current_income(state)
    state.manual_click.ready_at = now + MANUAL_CLICK.base_cooldown
    return True


def try_buy_income_upgrade(state: GameState) -> bool:
    cost = get_next_income_upgrade_cost(state)

    if state.score < cost:
        return False

    state.score -= cost
    state.manual_click.income_upgrade_level += 1
    return True
