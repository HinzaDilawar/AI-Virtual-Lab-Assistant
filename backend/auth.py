import bcrypt
import re

from backend.database import (
    user_exists_by_username,
    user_exists_by_email,
    insert_user,
    get_user_for_login,
    find_user_by_username_and_email,
    update_password_by_username,
)


def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())


def is_valid_username(username):
    # must be only letters/numbers/spaces/underscores, and contain at least one letter
    if not re.match(r'^[a-zA-Z0-9_ ]+$', username):
        return False
    if not re.search(r'[a-zA-Z]', username):
        return False
    return True


def is_valid_email(email):
    # only gmail.com addresses are accepted
    pattern = r'^[\w.-]+@gmail\.com$'
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
    if not is_valid_username(username):
        return False, "Username must contain letters — it cannot be only numbers, and can include spaces or underscores."
    if not email:
        return False, "Email cannot be empty."
    if not is_valid_email(email):
        return False, "Please use a valid Gmail address (e.g. ali@gmail.com)."

    strong, msg = is_strong_password(password)
    if not strong:
        return False, msg

    if user_exists_by_username(username):
        return False, "This username is already taken. Try another one."
    if user_exists_by_email(email):
        return False, "This email is already registered. Try logging in."

    try:
        insert_user(username, email, hash_password(password))
    except Exception:
        return False, "Something went wrong. Please try again."

    return True, "Account created successfully! You can now login."


def login(identifier, password):
    """Returns (ok: bool, message: str)"""
    identifier = identifier.strip()
    if not identifier or not password.strip():
        return False, "Please enter your username/email and password."

    looks_like_email = "@" in identifier

    if looks_like_email:
        identifier = identifier.lower()
        if not is_valid_email(identifier):
            return False, "Please enter a valid Gmail address or your correct username."
    else:
        if len(identifier) < 3 or not is_valid_username(identifier):
            return False, "Please enter a valid username or your correct Gmail address."

    row = get_user_for_login(identifier)
    if not row:
        return False, "Invalid credentials. Check your username/email or password."

    _id, uname, email, stored_hash = row
    if not verify_password(password, stored_hash):
        return False, "Invalid credentials. Check your username/email or password."

    return True, "Login successful."


def find_account(username, email):
    """Forgot password step 1: username + email dono match hone chahiye"""
    username = username.strip()
    email = email.strip().lower()

    if not username or not email:
        return False, "Please enter both your name and email."

    if not find_user_by_username_and_email(username, email):
        return False, "No account found with this name and email combination."

    return True, "Identity verified."


def reset_password(username, new_password):
    """Forgot password step 2: puzzle UI mein solve ho chuka hota hai, yahan sirf password set hota hai"""
    strong, msg = is_strong_password(new_password)
    if not strong:
        return False, msg

    update_password_by_username(username, hash_password(new_password))
    return True, "Password updated successfully. Please login."
