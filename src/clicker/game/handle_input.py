from ..app_state import Screen
from ..key_bindings import CommonKey, MenuKey, GameKey
from .new_game import new_game
from .manual_click import try_manual_click
from .buildings.economy import buy_building


def handle_input(key, app_state) -> None:

    if app_state.current_screen == Screen.MENU:
        handle_menu_input(key, app_state)
    elif app_state.current_screen == Screen.GAME:
        handle_game_input(key, app_state)
    else:
        raise ValueError(f"Unknown screen: {app_state.current_screen!r}")

def handle_menu_input(key, app_state) -> None:
    match key:
        case MenuKey.CONTINUE:
            if app_state.current_game is not None:
                app_state.current_screen = Screen.GAME
        case MenuKey.START:
            app_state.current_game = new_game()
            app_state.current_screen = Screen.GAME
        case MenuKey.QUIT:
            app_state.running = False
        case _:
            pass

def handle_game_input(key, app_state):
    match key:
        case GameKey.ESC:
            app_state.current_screen = Screen.MENU
        case GameKey.MANUAL_CLICK:
            try_manual_click(app_state.current_game)
        case _:
            pass
