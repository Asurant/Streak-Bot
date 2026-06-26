from slack_bolt import Ack, Respond
from logging import Logger
import sqlite3
from datetime import date
from slack_sdk import WebClient

def streakCommand(command, ack: Ack, respond: Respond, logger: Logger, client: WebClient):
    try:
        ack()
        userID = command["user_id"]
        conn = sqlite3.connect("streaks.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, streakName, currentStreak, lastCompletedDate from streaks WHERE userID = ?",
            (userID,)
        )
        streaks = cursor.fetchall()
        conn.close()

        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Streak Dashboard"
                }
            }
        ]
        if not streaks:
            blocks.append({
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "No streaks added."
                }
            })
        else:
            for id, streakName, currentStreak, lastCompletedDate in streaks:
                done = (lastCompletedDate == str(date.today()))
                status = ""
                if done:
                    status = "Completed"
                else:
                    status = "Not Completed"
                blocks.append({
                    "type": "divider"
                })
                blocks.append({
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*{streakName}*\nStreak: `{currentStreak} days` \n Status: {status}"
                    }
                })
        client.chat_postMessage(
            channel = userID,
            text = "Here is all of your streaks",
            blocks = blocks
        )
    except Exception as e:
        logger.error(e)
