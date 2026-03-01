import re

from config import ADMIN_EMAIL, ADMIN_PASSWORD
from database import get_connection, hash_password
import utils


def is_valid_email(email):
    return bool(re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email))


def login():
    utils.print_separator("LOGIN")
    conn = get_connection()
    cursor = conn.cursor()

    while True:
        email = input("Email: ").strip().lower()
        password = input("Password: ").strip()

        if email == ADMIN_EMAIL.lower() and password == ADMIN_PASSWORD:
            cursor.close()
            conn.close()
            return "admin"

        hashed = hash_password(password)
        cursor.execute(
            "SELECT name FROM users WHERE email = %s AND password_hash = %s",
            (email, hashed)
        )
        row = cursor.fetchone()
        if row:
            print(f"\nWelcome back, {row[0].capitalize()}!")
            cursor.close()
            conn.close()
            return email
        else:
            print("Incorrect email or password. Please try again.\n")


def signup():
    utils.print_separator("CREATE ACCOUNT")
    conn = get_connection()
    cursor = conn.cursor()

    name = utils.get_str_input("Full Name: ", max_length=100)

    while True:
        email = input("Email: ").strip().lower()
        if not is_valid_email(email):
            print("Invalid email address.")
            continue
        if email == ADMIN_EMAIL.lower():
            print("This email address cannot be used.")
            continue
        cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
        if cursor.fetchone():
            print("An account with this email already exists.")
            continue
        break

    while True:
        password = input("Password (min 6 characters): ").strip()
        if len(password) < 6:
            print("Password must be at least 6 characters.")
            continue
        if len(password) > 100:
            print("Password must be at most 100 characters.")
            continue
        confirm = input("Confirm Password: ").strip()
        if password != confirm:
            print("Passwords do not match.")
            continue
        break

    address = utils.get_str_input("Delivery Address: ", max_length=500)

    hashed = hash_password(password)
    cursor.execute(
        "INSERT INTO users (name, email, password_hash, address) VALUES (%s, %s, %s, %s)",
        (name, email, hashed, address)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print("\nAccount created successfully. You can now log in.")
