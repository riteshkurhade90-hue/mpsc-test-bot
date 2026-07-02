import sqlite3

DB_NAME = "quiz.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        name TEXT
    )
    """)

    conn.commit()
    conn.close()
def add_user(user_id, name):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "INSERT OR REPLACE INTO users(user_id, name) VALUES(?, ?)",
        (user_id, name)
    )

    conn.commit()
    conn.close()
