from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

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

def initialize_database():
    connection = create_connection()
    cursor = connection.cursor()

    try:
        # SQL to create database and table
        cursor.execute("CREATE DATABASE IF NOT EXISTS parthiban")
        cursor.execute("USE parthiban")
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

items = [
  {
    "id": 1,
    "name": "Trisha",
    "description": "An actress known for hb er work in Tamil and Telugu films."
  },
  {
    "id": 2,
    "name": "Nayanthara",
    "description": "A popular South Indian actress with a strong fan following."
  },
  {
    "id": 3,
    "name": "Sneha",
    "description": "An actress well-known for her roles in Tamil and Telugu cinema."
  },
  {
    "id": 4,
    "name": "Jyothika",
    "description": "A versatile actress who has won multiple awards for her performances."
  },
  {
    "id": 5,
    "name": "Samantha",
    "description": "An Indian actress known for her work in Tamil and Telugu films."
  }
]


# Route to get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

@app.route('/item/<int:id>', methods=['GET'])
def get_items_byid(id):
    return jsonify(items[id]), 200


@app.route('/item', methods=['POST'])
def post_item():
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("USE parthiban")
        cursor.execute("SELECT * FROM users")
        user = cursor.fetchall()
        if user:
            return jsonify(user), 200
        else:
            return jsonify("Sorry No user.")
    except Error as e:
        return jsonify(f"Error during login: {e}")
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)