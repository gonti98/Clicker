from dataclasses import dataclass


GROWTH_RATE: float = 1.15


@dataclass(frozen=True)
class BuildingDefinition:
    name: str
    base_cost: int
    base_income: int
    growth_rate: float = GROWTH_RATE

BUILDINGS = {
    "farm": BuildingDefinition(
        name="Farm",
        base_cost=10,
        base_income=1,
    ),
    "mine": BuildingDefinition(
        name="Mine",
        base_cost=100,
        base_income=10,
    ),
}
