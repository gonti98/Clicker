import curses

from .render.menu import draw_menu
from .render.game import draw_game
from .app_state import AppState, Screen
from .game.handle_input import handle_input


def app(stdscr) -> None:
    curses.curs_set(0)
    stdscr.timeout(100)
    stdscr.keypad(False)
    app_state = AppState()

    while app_state.running:
        key = stdscr.getch()
        handle_input(key, app_state)

        stdscr.erase()

        if app_state.current_screen == Screen.MENU:
            draw_menu(stdscr, app_state)
        elif app_state.current_screen == Screen.GAME:
            draw_game(stdscr, app_state.current_game)
        else:
            raise ValueError(f"Unknown screen: {app_state.current_screen!r}")

        stdscr.refresh()

def main():
    curses.wrapper(app)
