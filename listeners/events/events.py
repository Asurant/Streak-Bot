from logging import Logger
import sqlite3
from datetime import date
from slack_sdk import WebClient


def streakDashboard(client: WebClient, event: dict, logger: Logger):
    # ignore the app_home_opened event for anything but the Home tab
    if event["tab"] != "home":
        return
    try:
        userID = event["user"]
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
                blocks.append({
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Mark Streak As Completed"
                            },
                            "value": str(id),
                            "style": "primary",
                            "action_id": "createStreak" #Add the method for the button click future me
                        },
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Delete Streak"
                            },
                            "value": str(id),
                            "style": "primary",
                            "action_id": "deleteStreak" #Add the method for the button click future me
                        }
                    ]
                })
        blocks.append({
            "type": "actions",
            "elements": [{
                    "type": "button",
                    "style": "primary",
                    "action_id": "createStreak",
                    "text":{
                        "type": "plain_text",
                        "text": "Create New Streak"
                    }
                }
            ]
        })

        client.views_publish(
            user_id = userID,
            view={
                "type": "home",
                "blocks": blocks
            }
        )
        
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")
