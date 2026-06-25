import sqlite3
from datetime import date

STREAKS = "streaks.db"

def init_db():
    conn=sqlite3.connect("streaks.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS streaks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            userID TEXT NOT NULL,
            streakName TEXT NOT NULL,
            currentStreak INTEGER DEFAULT 0,
            lastCompletedDate TEXT
        )
    """)

    conn.commit()
    conn.close()

def addStreak(userID, streakName):
    conn=sqlite3.connect("streaks.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO streaks (userID, streakNAME) VALUES (?, ?)",
        (userID, streakName)
    )
    conn.commit()
    conn.close()

def deleteStreak(id):
    conn=sqlite3.connect("streaks.db")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM streaks WHERE id = ?",
        (id)
    )
    conn.commit()
    conn.close()

def getStreaks(userID):
    conn=sqlite3.connect("streaks.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, streakName, currentStreak, lastCompletedDate FROM streaks WHERE userID = ?",
        (userID)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

def completeStreak(id):
    conn = sqlite3.connect("streaks.db")
    cursor = conn.cursor()
    todayDate = str(date.today())
    cursor.execute("SELECT currentStreak, lastCompletedDate FROM streaks where id = ?",
        (id)
    )
    streak = cursor.fetchone()
    if streak:
        currentStreak, lastCompletedDate = streak
        if lastCompletedDate != todayDate:
            currentStreak += 1
            cursor.execute(
                "UPDATE streaks SET currentStreak = ?, lastCompletedDate = ? WHERE id = ?", (currentStreak, todayDate, id)
            )
            conn.commit()
    conn.close()

init_db()