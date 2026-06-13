import curses

from .game.new_game import new_game
from .render.menu import draw_menu
from .render.game import draw_game
from .game.buildings.economy import buy_building
from .game.manual_click import try_manual_click
from .app_state import AppState, Screen


def app(stdscr) -> None:
    curses.curs_set(0)
    stdscr.timeout(100)
    app_state = AppState()

    while app_state.running:
        stdscr.erase()

        if app_state.current_screen == Screen.MENU:
            draw_menu(stdscr)
        elif app_state.current_screen == Screen.GAME:
            draw_game(stdscr, app_state.current_game)
        else:
            raise ValueError(f"Unknown screen: {app_state.current_screen!r}")

        stdscr.refresh()
        key = stdscr.getch()

        if key == ord("q"):
            app_state.running = False

        elif key == ord("s") and app_state.current_screen == Screen.MENU:
            app_state.current_game = new_game()
            app_state.current_screen = Screen.GAME

        elif key == ord(" ") and app_state.current_screen == Screen.GAME:
            if app_state.current_game is not None:
                try_manual_click(app_state.current_game)

        elif key == ord("1") and app_state.current_screen == Screen.GAME:
            if app_state.current_game is not None:
                buy_building(app_state.current_game, "farm")

def main():
    curses.wrapper(app)
