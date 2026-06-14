from dataclasses import dataclass


GROWTH_RATE: float = 1.15


@dataclass(frozen=True)
class ManualClickDefinition:
    base_income: int
    base_income_upgrade_cost: int
    income_increment_per_level: int
    base_cooldown: float
    growth_rate: float = GROWTH_RATE


MANUAL_CLICK = ManualClickDefinition(
    base_income=1,
    base_income_upgrade_cost=100,
    income_increment_per_level=1,
    base_cooldown=1.0,
)
