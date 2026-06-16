import re
import hashlib
from backend.database import create_connection

def hash_password(password):
    """Password ko hash karo secure storage ke liye"""
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_email(email):
    """Email format check karo"""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

def is_strong_password(password):
    """
    Password rules:
    - Min 8 characters
    - At least 1 uppercase letter
    - At least 1 number
    - At least 1 special character
    """
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
    """
    Register new user with email + strong password.
    Returns: (success: bool, message: str)
    """
    # --- Validations ---
    if not username.strip():
        return False, "Username cannot be empty."
    if len(username.strip()) < 3:
        return False, "Username must be at least 3 characters."
    if not re.match(r'^[a-zA-Z0-9_]+$', username.strip()):
        return False, "Username can only contain letters, numbers, and underscores."
    if not email.strip():
        return False, "Email cannot be empty."
    if not is_valid_email(email.strip()):
        return False, "Please enter a valid email address (e.g. ali@gmail.com)."
    
    strong, msg = is_strong_password(password)
    if not strong:
        return False, msg

    # --- Save to DB ---
    conn = create_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username.strip(), email.strip().lower(), hash_password(password))
        )
        conn.commit()
        return True, f"Account created successfully! Welcome, {username} 🎉"
    except Exception as e:
        err = str(e)
        if "username" in err:
            return False, "This username is already taken. Try another one."
        elif "email" in err:
            return False, "This email is already registered. Try logging in."
        return False, "Something went wrong. Please try again."
    finally:
        conn.close()

def login(username_or_email, password):
    """
    Login with username OR email + password.
    Returns: bool
    """
    if not username_or_email.strip() or not password.strip():
        return False

    conn = create_connection()
    cur = conn.cursor()
    hashed = hash_password(password)

    # Allow login with either username or email
    cur.execute(
        "SELECT * FROM users WHERE (username=? OR email=?) AND password=?",
        (username_or_email.strip(), username_or_email.strip().lower(), hashed)
    )
    user = cur.fetchone()
    conn.close()
    return user is not None

