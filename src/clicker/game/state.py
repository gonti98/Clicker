from dataclasses import dataclass, field


@dataclass
class BuildingState:
    count: int = 0


@dataclass
class ManualClickState:
    ready_at: float = 0.0
    income_upgrade_level: int = 0


@dataclass
class GameState:
    score: float = 0.0
    total_score: float = 0.0
    total_time_played: float = 0.0
    buildings: dict[str, BuildingState] = field(default_factory=dict)
    manual_click: ManualClickState = field(default_factory=ManualClickState)
