import time


def handle_manual_score(current_game):
    now = time.monotonic()
    manual_click = current_game.manual_click

    if now >= manual_click.ready_at:
        current_game.score += manual_click.value
        manual_click.ready_at = now + manual_click.cooldown
