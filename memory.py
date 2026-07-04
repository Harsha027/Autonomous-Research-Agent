import json
import os

HISTORY_FILE = "memory/history.json"


def save_history(topic):
    """
    Save searched topics to history.json.
    """

    os.makedirs("memory", exist_ok=True)

    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as file:
            json.dump([], file)

    try:
        with open(HISTORY_FILE, "r") as file:
            history = json.load(file)
    except Exception:
        history = []

    if not history or history[-1].lower() != topic.lower():
        history.append(topic)

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def get_history():
    """
    Return all previous searches.
    """

    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    except Exception:
        return []