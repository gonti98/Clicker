from .state import Screen
from .key_bindings import MenuKey, GameKey
from .save_manager import save, load, has_save
from ..game.new_game import new_game
from ..game.manual.economy import try_manual_click, try_buy_income_upgrade
from ..game.buildings.economy import try_buy_building


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
            if has_save:
                app_state.current_game = load()
                app_state.current_screen = Screen.GAME
        case MenuKey.START:
            app_state.current_game = new_game()
            app_state.current_screen = Screen.GAME
        case MenuKey.QUIT:
            app_state.running = False
        case _:
            pass


def handle_game_input(key, app_state):
    building_keys = list(app_state.current_game.buildings)

    match key:
        case GameKey.ESC:
            app_state.current_screen = Screen.MENU
            save(app_state.current_game)
        case GameKey.MANUAL_CLICK:
            try_manual_click(app_state.current_game)
        case GameKey.BUY_BUILDING_1:
            try_buy_building(app_state.current_game, building_keys[0])
        case GameKey.BUY_BUILDING_2:
            try_buy_building(app_state.current_game, building_keys[1])
        case GameKey.MANUAL_CLICK_UPGRADE:
            try_buy_income_upgrade(app_state.current_game)
        case _:
            pass
