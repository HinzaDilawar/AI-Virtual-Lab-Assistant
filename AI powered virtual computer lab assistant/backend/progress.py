import sqlite3

DB_NAME = "fyp.db"

def create_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # rows ko dict jaise access karne ke liye
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Progress table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            topic TEXT,
            status TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(username) REFERENCES users(username)
        )
    """)

    conn.commit()
    conn.close()

def add_progress(username, topic, status="Attempted"):
    conn = create_connection()
    cursor = conn.cursor()
    # Already attempted same topic? agar yes to update status
    cursor.execute("SELECT id FROM progress WHERE username=? AND topic=?", (username, topic))
    row = cursor.fetchone()
    if row:
        cursor.execute("UPDATE progress SET status=?, timestamp=CURRENT_TIMESTAMP WHERE id=?", (status, row["id"]))
    else:
        cursor.execute("INSERT INTO progress (username, topic, status) VALUES (?, ?, ?)", (username, topic, status))
    conn.commit()
    conn.close()

# ✅ New function: fetch all progress
def fetch_all_progress():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username, topic, status, timestamp FROM progress ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    # convert rows to list of dict
    return [dict(row) for row in rows]

# ✅ Add this function for teacher dashboard
def get_progress():
    return fetch_all_progress()  # same data as fetch_all_progress

# Run once to create tables
create_tables()
