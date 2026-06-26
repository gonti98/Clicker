from enum import IntEnum


class BaseKey(IntEnum):
    label: str
    description: str

    def __new__(cls, value: int, label: str, description: str):
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.label = label
        obj.description = description
        return obj


class CommonKey(BaseKey):
    LEFT = (ord("h"), "h", "Left")
    DOWN = (ord("j"), "j", "Down")
    UP = (ord("k"), "k", "Up")
    RIGHT = (ord("l"), "l", "Right")


class MenuKey(BaseKey):
    CONTINUE = (ord("c"), "c", "Continue")
    START = (ord("s"), "s", "Start new game")
    QUIT = (ord("q"), "q", "Quit")


class GameKey(BaseKey):
    MANUAL_CLICK = (ord(" "), "space", "Manual score")
    MANUAL_CLICK_UPGRADE = (ord("v"), "v", "Upgrade manual score")
    BUY_BUILDING_1 = (ord("1"), "1", "Buy 1")
    BUY_BUILDING_2 = (ord("2"), "2", "Buy 2")
    ESC = (27, "esc", "Escape")
