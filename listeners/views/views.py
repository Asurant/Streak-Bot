from logging import Logger
from datetime import date
from slack_bolt import Ack
from slack_sdk import WebClient
import database

def addStreak(view, ack: Ack, body: dict, client: WebClient, logger: Logger):
    try:
        ack()
        streakName = view["state"]["values"]["inputBlock"]["streakName"]["value"]
        userID = body["user"]["id"]
        database.addStreak(userID, streakName)
    except Exception as e:
        logger.error(e)