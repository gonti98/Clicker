from .text import center_string


def draw_menu(stdscr) -> None:
    height, width = stdscr.getmaxyx()
    stdscr.addstr(0, 0, f"Size: {height}x{width}")
    center_string(stdscr, "press [s] to start")
