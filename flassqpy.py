from flask import Flask 
import mysql.connector
from mysql.connector import Error

try:
    # Establish a connection to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Angel@1408",
        database="parthidb1" 
    )
    
    if connection.is_connected():
        print("The connection is connected")

        # Create a cursor object
        cursor = connection.cursor()

        # Define and execute the query
        query = "SELECT * FROM employees "
        cursor.execute(query)

        # Fetch the results
        result = cursor.fetchall()

        # Iterate through the results and print each row
        for row in result:
            print(row)

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        connection.close()
        print("The connection is closed")
