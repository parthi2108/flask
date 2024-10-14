import mysql.connector
from mysql.connector import Error

def fetch_data():
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host='localhost',
            database='students',
            user='root',
            password='Angel@1408'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM  department ;")
            rows = cursor.fetchall()

            # Print fetched data
            for row in rows:
                 print(f"The name of the student is: {row[1]}")
                 print(f"The class of the student is : {row[2]}")
                 print(f"The  of the student is : {row[3]}")
    
    except Error as e:
        print("Error while fetching data from MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
fetch_data()
