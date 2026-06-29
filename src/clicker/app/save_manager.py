import json
from pathlib import Path

from ..game.state import GameState
from ..game.new_game import new_game

SAVE_DIR = Path("./saves/")
SAVE_FILE = SAVE_DIR / "save.json"
SAVE_VERSION = "1"


def has_save() -> bool:
    return SAVE_FILE.is_file()


def save(current_game: GameState) -> None:
    buildings_data = {
        building_name: {"count": building_state.count}
        for building_name, building_state in current_game.buildings.items()
    }

    data = {
        "save_version": SAVE_VERSION,
        "game_version": "0.0.1",
        "resources": {"score": current_game.score},
        "buildings": buildings_data,
        "manual_click": {
            "income_upgrade_level": current_game.manual_click.income_upgrade_level
        },
        "stats": {
            "total_time_played": current_game.total_time_played,
            "total_score": current_game.total_score,
        },
        "prestige": {},
    }

    SAVE_DIR.mkdir(parents=True, exist_ok=True)

    with SAVE_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def validate_save_data(data) -> None:
    if not isinstance(data, dict):
        raise ValueError("Wrong file format")

    if "save_version" not in data:
        raise ValueError("File corrupted")

    if data["save_version"] != SAVE_VERSION:
        raise ValueError("Unsupported save version")

    if "resources" not in data:
        raise ValueError("File corrupted")
    if not isinstance(data["resources"], dict):
        raise ValueError("Wrong file format")
    if "score" not in data["resources"]:
        raise ValueError("File corrupted")

    if "buildings" not in data:
        raise ValueError("File corrupted")
    if not isinstance(data["buildings"], dict):
        raise ValueError("Wrong file format")

    if "manual_click" not in data:
        raise ValueError("File corrupted")
    if not isinstance(data["manual_click"], dict):
        raise ValueError("Wrong file format")
    if "income_upgrade_level" not in data["manual_click"]:
        raise ValueError("File corrupted")

    if "stats" not in data:
        raise ValueError("File corrupted")
    if not isinstance(data["stats"], dict):
        raise ValueError("Wrong file format")
    if "total_score" not in data["stats"]:
        raise ValueError("File corrupted")
    if "total_time_played" not in data["stats"]:
        raise ValueError("File corrupted")


def load() -> GameState:
    if not has_save():
        raise FileNotFoundError("Save file does not exist")

    try:
        with SAVE_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as exc:
        raise ValueError("Save file is corrupted") from exc

    validate_save_data(data)

    game_state = new_game()

    game_state.score = data["resources"]["score"]
    game_state.manual_click.income_upgrade_level = data["manual_click"][
        "income_upgrade_level"
    ]
    game_state.total_time_played = data["stats"]["total_time_played"]
    game_state.total_score = data["stats"]["total_score"]

    for building_name, building_data in data["buildings"].items():
        if building_name in game_state.buildings:
            game_state.buildings[building_name].count = building_data["count"]

    return game_state
