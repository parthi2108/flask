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
            cursor.execute ("""SELECT 
    students.Name AS Student_name, 
    student_parents_hobbies.Hobbies AS Student_hobby, 
    student_address_transportation.Transportation AS Student_Commute
FROM 
    students
INNER JOIN 
    student_parents_hobbies ON students.RollNo = student_parents_hobbies.RollNo
INNER JOIN 
    student_address_transportation ON students.RollNo = student_address_transportation.RollNo;
""")
            rows = cursor.fetchall()

            # Print fetched data
            for row in rows:
                print(f"The Name of the student is : {row[0]}")
                print(f"The Hobby of the student is : {row[1]}")
                print(f"The Commute mode of the student is : {row[2]}")
                
                
                #  print(f"The name of the student is: {row[1]}")
                #  print(f"The class of the student is : {row[2]}")
                #  print(f"The country of the student is : {row[4]}")
    
    except Error as e:
        print("Error while fetching data from MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

fetch_data()