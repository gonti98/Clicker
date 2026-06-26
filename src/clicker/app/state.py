from dataclasses import dataclass
from enum import Enum

from ..game.state import GameState


class Screen(Enum):
    MENU = "menu"
    GAME = "game"


@dataclass
class AppState:
    current_screen: Screen = Screen.MENU
    current_game: GameState | None = None
    running: bool = True
