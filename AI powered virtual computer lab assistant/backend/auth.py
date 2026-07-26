import re
import hashlib
import random
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

from backend.database import (
    create_connection,
    user_exists_by_username,
    user_exists_by_email,
    get_user_by_email,
    set_reset_code,
    verify_reset_code,
    update_password,
)

# ================= Gmail SMTP Config =================
# 1. Gmail account mein 2-Step Verification on karo
# 2. myaccount.google.com/apppasswords se 16-digit App Password banao
# 3. Neeche apna Gmail + wo App Password daalo
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_EMAIL = "yourapp@gmail.com"          # <-- apna Gmail yahan
SMTP_APP_PASSWORD = "xxxx xxxx xxxx xxxx"  # <-- App Password yahan (spaces ke sath ya bina)
# =======================================================


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None


def is_strong_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter (A-Z)."
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one number (0-9)."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character (!@#$...)."
    return True, "Password is strong."


def signup(username, email, password):
    username = username.strip()
    email = email.strip().lower()

    if not username:
        return False, "Username cannot be empty."
    if len(username) < 3:
        return False, "Username must be at least 3 characters."
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False, "Username can only contain letters, numbers, and underscores."
    if not email:
        return False, "Email cannot be empty."
    if not is_valid_email(email):
        return False, "Please enter a valid email address (e.g. ali@gmail.com)."

    strong, msg = is_strong_password(password)
    if not strong:
        return False, msg

    # 🔑 Ye check pehle missing tha — ab signup se PEHLE verify karta hai
    if user_exists_by_username(username):
        return False, "This username is already taken. Try another one."
    if user_exists_by_email(email):
        return False, "This email is already registered. Try logging in."

    conn = create_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, hash_password(password))
        )
        conn.commit()
        return True, f"Account created successfully! Welcome, {username} 🎉"
    except Exception:
        return False, "Something went wrong. Please try again."
    finally:
        conn.close()


def login(username_or_email, password):
    if not username_or_email.strip() or not password.strip():
        return False
    conn = create_connection()
    cur = conn.cursor()
    hashed = hash_password(password)
    cur.execute(
        "SELECT * FROM users WHERE (username=? OR email=?) AND password=?",
        (username_or_email.strip(), username_or_email.strip().lower(), hashed)
    )
    user = cur.fetchone()
    conn.close()
    return user is not None


# ================= Forgot Password =================

def _send_reset_email(to_email, code):
    body = f"Your Virtual Lab password reset code is: {code}\nThis code expires in 10 minutes."
    msg = MIMEText(body)
    msg["Subject"] = "Virtual Lab - Password Reset Code"
    msg["From"] = SMTP_EMAIL
    msg["To"] = to_email
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_APP_PASSWORD.replace(" ", ""))
        server.sendmail(SMTP_EMAIL, to_email, msg.as_string())


def request_password_reset(email):
    email = email.strip().lower()
    if not get_user_by_email(email):
        return False, "No account found with this email."
    code = str(random.randint(100000, 999999))
    expiry = (datetime.now() + timedelta(minutes=10)).isoformat()
    set_reset_code(email, code, expiry)
    try:
        _send_reset_email(email, code)
    except Exception as e:
        return False, f"Could not send email: {e}"
    return True, "Reset code sent to your email."


def reset_password(email, code, new_password):
    email = email.strip().lower()
    if not code.strip():
        return False, "Please enter the code sent to your email."
    if not verify_reset_code(email, code.strip()):
        return False, "Invalid or expired code."
    strong, msg = is_strong_password(new_password)
    if not strong:
        return False, msg
    update_password(email, hash_password(new_password))
    return True, "Password updated successfully. Please login."

