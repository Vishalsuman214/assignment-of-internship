import hashlib
import sqlite3
import os

def create_db():
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL,
            email TEXT NOT NULL,
            forget_password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup(username, password, email):
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    password_hash = hash_password(password)
    try:
        c.execute("INSERT INTO users(username, password_hash, email, forget_password) VALUES (?, ?, ?, ?)",
                  (username, password_hash, email, ""))
        conn.commit()
        print("Signup successful!")
    except sqlite3.IntegrityError:
        print("Username already exists!")
    finally:
        conn.close()

def login(username, password):
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    password_hash = hash_password(password)
    c.execute("SELECT * FROM users WHERE username=? AND password_hash=?", (username, password_hash))
    user = c.fetchone()
    conn.close()
    return bool(user)

def reset_password(username):
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()
    if user:
        new_password = input("Enter new password: ").strip()
        if not new_password:
            print("Password cannot be empty!")
        else:
            new_password_hash = hash_password(new_password)
            c.execute("UPDATE users SET password_hash=? WHERE username=?", (new_password_hash, username))
            conn.commit()
            print("Password updated successfully!")
    else:
        print("Invalid username!")
    conn.close()

def main():
    create_db()
    print("Welcome to login portal")
    while True:
        print("\n1. login\n2. signup\n3. reset password\n4. exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            username = input("Username: ").strip()
            if not username:
                print("Username cannot be empty!")
                continue
            password = input("Password: ").strip()
            if not password:
                print("Password cannot be empty!")
                continue
            if login(username, password):
                print("Login successful!")
            else:
                print("Invalid user!")
        elif choice == "2":
            username = input("Enter Username: ").strip()
            if not username:
                print("Username cannot be empty!")
                continue
            password = input("Enter Password: ").strip()
            if not password:
                print("Password cannot be empty!")
                continue
            email = input("Enter Email: ").strip()
            if not email:
                print("Email cannot be empty!")
                continue
            signup(username, password, email)
        elif choice == "3":
            username = input("Enter username: ").strip()
            if not username:
                print("Username cannot be empty!")
                continue
            reset_password(username)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
