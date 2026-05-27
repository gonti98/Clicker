from .text import center_string


def draw_game(stdscr, current_game: GameState) -> None:
    center_string(stdscr, str(current_game.score))
