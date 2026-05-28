import curses
from .game.new_game import new_game
from .render.menu import draw_menu
from .render.game import draw_game
from .game.buildings.economy import buy_building


SCREEN_MENU = "menu"
SCREEN_GAME = "game"


def app(stdscr) -> None:
    curses.curs_set(0)
    stdscr.timeout(100)
    current_game = None
    current_screen = SCREEN_MENU

    while True:
        stdscr.erase()

        if current_screen == SCREEN_MENU:
            draw_menu(stdscr)
        elif current_screen == SCREEN_GAME:
            draw_game(stdscr, current_game)

        stdscr.refresh()
        key = stdscr.getch()

        if key == ord("q"):
            break
        elif key == ord(" ") and current_screen == SCREEN_GAME:
            current_game.score += 1
        elif key == ord("s")  and current_screen == SCREEN_MENU:
            current_screen = SCREEN_GAME
            current_game = new_game()
        elif key == ord("1") and current_screen == SCREEN_GAME:
            buy_building(current_game, "farm")

def main():
    curses.wrapper(app)
