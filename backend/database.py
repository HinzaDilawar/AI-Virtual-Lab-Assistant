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
    # Purani DB mein columns nahi hongi to add kar do (agar already hain to ignore)
    for col in ["reset_code TEXT", "reset_expiry TEXT"]:
        try:
            cur.execute(f"ALTER TABLE users ADD COLUMN {col}")
        except sqlite3.OperationalError:
            pass
    conn.commit()
    conn.close()

# ---------------- 🔑 Naye functions (duplicate check ke liye) ----------------

def user_exists_by_username(username):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM users WHERE username=?", (username,))
    exists = cur.fetchone() is not None
    conn.close()
    return exists

def user_exists_by_email(email):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM users WHERE email=?", (email,))
    exists = cur.fetchone() is not None
    conn.close()
    return exists

def get_user_by_email(email):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, username, email FROM users WHERE email=?", (email,))
    row = cur.fetchone()
    conn.close()
    return row

def set_reset_code(email, code, expiry_iso):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET reset_code=?, reset_expiry=? WHERE email=?", (code, expiry_iso, email))
    conn.commit()
    conn.close()

def verify_reset_code(email, code):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT reset_code, reset_expiry FROM users WHERE email=?", (email,))
    row = cur.fetchone()
    conn.close()
    if not row or row[0] is None:
        return False
    stored_code, expiry = row
    if stored_code != code:
        return False
    from datetime import datetime
    if expiry and datetime.now() > datetime.fromisoformat(expiry):
        return False
    return True

def update_password(email, new_hashed_password):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET password=?, reset_code=NULL, reset_expiry=NULL WHERE email=?",
        (new_hashed_password, email)
    )
    conn.commit()
    conn.close()

create_table()