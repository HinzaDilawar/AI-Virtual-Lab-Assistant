import sqlite3

DB_NAME = "fyp.db"


def create_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def user_exists_by_username(username):
    conn = create_connection(); cur = conn.cursor()
    cur.execute("SELECT 1 FROM users WHERE username=?", (username,))
    exists = cur.fetchone() is not None
    conn.close()
    return exists


def user_exists_by_email(email):
    conn = create_connection(); cur = conn.cursor()
    cur.execute("SELECT 1 FROM users WHERE email=?", (email,))
    exists = cur.fetchone() is not None
    conn.close()
    return exists


def insert_user(username, email, hashed_password):
    conn = create_connection(); cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
        (username, email, hashed_password)
    )
    conn.commit()
    conn.close()


def get_user_for_login(identifier):
    """identifier = username ya email. Returns (id, username, email, password) ya None"""
    conn = create_connection(); cur = conn.cursor()
    cur.execute(
        "SELECT id, username, email, password FROM users WHERE username=? OR email=?",
        (identifier, identifier.lower())
    )
    row = cur.fetchone()
    conn.close()
    return row


def find_user_by_username_and_email(username, email):
    """Forgot password ke liye — dono match hone chahiye"""
    conn = create_connection(); cur = conn.cursor()
    cur.execute(
        "SELECT id FROM users WHERE username=? AND email=?",
        (username, email.lower())
    )
    row = cur.fetchone()
    conn.close()
    return row is not None


def update_password_by_username(username, new_hashed_password):
    conn = create_connection(); cur = conn.cursor()
    cur.execute("UPDATE users SET password=? WHERE username=?", (new_hashed_password, username))
    conn.commit()
    conn.close()


create_table()
