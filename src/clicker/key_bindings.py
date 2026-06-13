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
    MANUAL_CLICK = (ord(" "), "SPACE", "Manual score")
    BUY_FARM = (ord("1"), "1", "Buy Farm")
    ESC = (27, "esc", "Escape")
