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
        print("Connected to the database")
        
        # Create a cursor
        cursor = connection.cursor()
        
        # Write and execute the query
        query = "SELECT * FROM employees where Name ='John Doe' " 
        
        cursor.execute(query)
        
        # Fetch all rows
        rows = cursor.fetchall()
        
        # Loop through the rows and print them
        for row in rows:
            print(row)
    
except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed")
