import curses
import time

from .render.menu import draw_menu
from .render.game import draw_game
from .app.state import AppState, Screen
from .app.handle_input import handle_input
from .game.update import update_game


def app(stdscr) -> None:
    curses.curs_set(0)
    stdscr.timeout(100)
    stdscr.keypad(False)
    app_state = AppState()
    last_frame_time = time.monotonic()

    while app_state.running:
        current_time = time.monotonic()
        delta_time = current_time - last_frame_time
        last_frame_time = current_time
        key = stdscr.getch()
        handle_input(key, app_state)

        stdscr.erase()

        if app_state.current_screen == Screen.MENU:
            draw_menu(stdscr)
        elif app_state.current_screen == Screen.GAME:
            game = app_state.current_game
            if game is None:
                raise ValueError("current_game is None on GAME screen")

            update_game(game, delta_time)
            draw_game(stdscr, game)
        else:
            raise ValueError(f"Unknown screen: {app_state.current_screen!r}")

        stdscr.refresh()


def main():
    curses.wrapper(app)
