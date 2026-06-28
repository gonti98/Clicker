import curses

from ..app.key_bindings import MenuKey
from .text import center_string_offset


def draw_menu(stdscr, app_state) -> None:
    height, width = stdscr.getmaxyx()
    stdscr.addstr(0, 0, f"Size: {height}x{width}")

    for offset_y, key in enumerate(MenuKey):
        attr = (
            curses.A_DIM
            if key is MenuKey.CONTINUE and app_state.current_game is None
            else 0
        )

        center_string_offset(stdscr, key.description, offset_y, 0, attr)
