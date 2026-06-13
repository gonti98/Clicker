import curses


def safe_addstr(stdscr, y: int, x: int, text: str, attr: int = 0) -> None:
    height, width = stdscr.getmaxyx()

    if y < 0 or y >= height:
        return

    if x < 0:
        text = text[-x:]
        x = 0

    if x >= width:
        return

    text = text[: width - x]

    if not text:
        return

    try:
        stdscr.addstr(y, x, text, attr)
    except curses.error:
        pass


def center_string(stdscr, text: str, attr: int = 0) -> None:
    height, width = stdscr.getmaxyx()
    center_height = height // 2
    center_width = (width - len(text)) // 2
    safe_addstr(stdscr, center_height, center_width, text, attr)


def center_string_offset(
    stdscr,
    text: str,
    offset_y: int,
    offset_x: int,
    attr: int = 0,
    ) -> None:

    height, width = stdscr.getmaxyx()
    center_height = (height // 2) + offset_y
    center_width = ((width - len(text)) // 2) + offset_x
    safe_addstr(stdscr, center_height, center_width, text, attr)
