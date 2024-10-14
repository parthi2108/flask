

import mysql.connector
from mysql.connector import Error

def add_column_and_insert_countries():
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            database='students',  # Replace with your actual database name
            user='root',          # Replace with your MySQL username
            password='Angel@1408' # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Check if the 'country' column exists, and if not, add it
            cursor.execute("SHOW COLUMNS FROM students LIKE 'country';")
            result = cursor.fetchone()

            if not result:
                # If 'country' column doesn't exist, add it
                cursor.execute("ALTER TABLE students ADD COLUMN country VARCHAR(100) where RollNo =1-50 ;")
                print("Added 'country' column to the table.")

            # List of 50 countries
            countries = [
                'India', 'USA', 'UK', 'Canada', 'Australia', 'Germany', 'France', 'Japan', 'China', 'Brazil',
                'Russia', 'South Korea', 'Mexico', 'Spain', 'Italy', 'Netherlands', 'Sweden', 'Switzerland', 
                'Argentina', 'South Africa', 'New Zealand', 'Singapore', 'Malaysia', 'Thailand', 'Vietnam', 
                'Philippines', 'Indonesia', 'Norway', 'Denmark', 'Finland', 'Poland', 'Portugal', 'Greece', 
                'Turkey', 'Egypt', 'Saudi Arabia', 'UAE', 'Pakistan', 'Bangladesh', 'Sri Lanka', 'Nepal', 
                'Ireland', 'Belgium', 'Austria', 'Hungary', 'Czech Republic', 'Romania', 'Ukraine', 'Israel', 
                'Chile', 'Colombia'
            ]

            for roll_no, country in enumerate(countries, start=1):
                update_query = "UPDATE students SET country = %s WHERE RollNo = %s"
                cursor.execute(update_query, (country, roll_no))

            # Commit the changes to the database
            connection.commit()
            print("Country data inserted successfully.")

    except Error as e:
        print(f"Error while modifying table or inserting data into MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Call the function to add column and insert country data
add_column_and_insert_countries()
