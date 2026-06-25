from logging import Logger
from datetime import date
from slack_bolt import Ack
from slack_sdk import WebClient
import database

def createStreak(ack: Ack, body: dict, client: WebClient, logger: Logger):
    try:
        ack()
        client.views_open(
            trigger_id=body["trigger_id"],
            view={
                "type": "modal",
                "callback_id": "createStreak",
                "title": {
                    "type": "plain_text",
                    "text": "Create A New Streak"
                },
                "submit": {
                    "type": "plain_text",
                    "text": "Add Streak"
                },
                "close": {
                    "type": "plain_text",
                    "text": "Cancel"
                },
                "blocks": [{
                    "type": "input",
                    "block_id": "inputBlock",
                    "label": {
                        "type": "plain_text",
                        "text": "Add Streak"
                    },
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "streakName"
                    }
                }]
            }
        )
    except Exception as e:
        logger.error(e)

def completeStreak(ack: Ack, body: dict, client: WebClient, logger: Logger):
    try:
        ack()
        id = int(body["actions"][0]["value"])
        database.completeStreak(id, str(date.today()))
    except Exception as e:
        logger.error(e)

def deleteStreak(ack: Ack, body: dict, client: WebClient, logger: Logger):
    try:
        ack()
        id = int(body["actions"][0]["value"])
        database.deleteStreak(id)
    except Exception as e:
        logger.error(e)