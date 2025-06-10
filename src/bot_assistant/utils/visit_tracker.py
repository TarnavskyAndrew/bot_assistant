import json
from datetime import datetime, timedelta
from bot_assistant.utils.logger import logger
from bot_assistant.utils.translate import translate
from bot_assistant.utils.path_config import LAST_VISIT_FILE
from pathlib import Path


def save_visit_now():
    now = datetime.now().isoformat()
    try:
        with open(LAST_VISIT_FILE, "w", encoding="utf-8") as file:
            json.dump({"timestamp": now}, file)
        logger.info("Last visit saved: %s", now)
    except Exception as e:
        logger.error("Failed to save visit time: %s", e)


def get_last_visit_message() -> str:
    if not LAST_VISIT_FILE.exists():
        logger.info("Visit file not found, assuming first visit.")
        return translate("first_visit")

    try:
        with open(LAST_VISIT_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            last_visit = datetime.fromisoformat(data["timestamp"])

        now = datetime.now()
        delta = now - last_visit

        days = delta.days
        hours = delta.seconds // 3600
        
        logger.info("Last visit was %s days and %s hours ago", days, hours)

        if days == 0 and hours == 0:
            return translate("welcome_back_soon")

        if days > 0:
            return translate("visit_message_days").format(days=days, hours=hours)
        else:
            return translate("visit_message_hours").format(hours=hours)

    except Exception:
        logger.error("Error parsing visit file: %s", e)
        return translate("visit_parse_error")
    