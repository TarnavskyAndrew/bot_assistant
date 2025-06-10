from bot_assistant.utils.path_config import JOKES_FILE
from bot_assistant.utils.config import get_lang
from bot_assistant.utils.logger import logger
import json
import random


def get_random_joke():
    lang = get_lang()
    try:
        with open(JOKES_FILE, "r", encoding="utf-8") as file:
            jokes = json.load(file)
        return random.choice(jokes.get(lang, []))
    except Exception as e:
        logger.warning(f"Could not load joke: {e}")
        return ""
