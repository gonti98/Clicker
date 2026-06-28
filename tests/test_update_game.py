from clicker.game.state import GameState, BuildingState
from clicker.game.update import update_game


def test_update_game_increases_total_time_played():
    state = GameState(total_time_played=0.0)

    update_game(state, 1.5)

    assert state.total_time_played == 1.5


def test_update_game_increases_score_from_buildings():
    state = GameState(
        score=0.0,
        buildings={
            "farm": BuildingState(count=1),
        },
    )

    update_game(state, 1.0)

    assert state.score > 0.0
