def center_string(stdscr, text: str) -> None:
    height, width = stdscr.getmaxyx()
    center_height = height // 2
    center_width = (width - len(text)) // 2
    stdscr.addstr(center_height, center_width, text)
