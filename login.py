import mysql.connector
from mysql.connector import Error
import hashlib

# Database connection setup
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="Angel@1408"  # Replace with your MySQL password
        )
        if connection.is_connected():
            print("Connected to MySQL server")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Create database and table if not exists
def initialize_database():
    connection = create_connection()
    cursor = connection.cursor()

    try:
        # SQL to create database and table
        cursor.execute("CREATE DATABASE IF NOT EXISTS user_auth")
        cursor.execute("USE user_auth")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE
            )
        """)
        print("Database and table initialized.")
    except Error as e:
        print(f"Error initializing database: {e}") 
    finally:
        cursor.close()
        connection.close()

# Function to hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register a new user
def register_user(username, password, email):
    connection = create_connection()
    cursor = connection.cursor()

    hashed_password = hash_password(password)

    try:
        cursor.execute("USE user_auth")
        cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", 
                       (username, hashed_password, email))
        connection.commit()
        print("User registered successfully!")
    except Error as e:
        print(f"Failed to register user: {e}")
    finally:
        cursor.close()
        connection.close()

# User login function
def login_user(username, password):
    connection = create_connection()
    cursor = connection.cursor()

    hashed_password = hash_password(password)

    try:
        cursor.execute("USE user_auth")
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", 
                       (username, hashed_password))
        user = cursor.fetchone()
        if user:
            print(f"Login successful! Welcome, {username}.")
        else:
            print("Login failed. Invalid username or password.")
    except Error as e:
        print(f"Error during login: {e}")
    finally:
        cursor.close()
        connection.close()

# Main program loop
def main():
    initialize_database()  # Initialize the database and table when the program starts

    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            register_user(username, password, email)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            login_user(username, password)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
