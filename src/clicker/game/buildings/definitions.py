from dataclasses import dataclass


GROWTH_RATE: float = 1.15


@dataclass(frozen=True)
class BuildingDefinition:
    name: str
    base_building_cost: int
    base_income: int
    base_income_cost: int
    base_cooldown: float
    growth_rate: float = GROWTH_RATE


BUILDINGS = {
    "farm": BuildingDefinition(
        name="Farm",
        base_building_cost=10,
        base_income=1,
        base_income_cost=100,
        base_cooldown=1.0,
    ),
    "mine": BuildingDefinition(
        name="Mine",
        base_building_cost=100,
        base_income=10,
        base_income_cost=1000,
        base_cooldown=2.0,
    ),
}
