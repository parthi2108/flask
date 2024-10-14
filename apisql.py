# import mysql.connector
# from mysql.connector import Error

# def create_table():
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             database='students',  # Replace with your database name
#             user='root',               # Replace with your MySQL username
#             password='Angel@1408'   # Replace with your MySQL password
#         )

#         if connection.is_connected():
#             cursor = connection.cursor()

#             create_table_query = """
#             CREATE TABLE IF NOT EXISTS user_info (
#                 gender VARCHAR(10),
#                 title VARCHAR(10),
#                 first_name VARCHAR(50),
#                 last_name VARCHAR(50),
#                 street_number INT,
#                 street_name VARCHAR(100),
#                 city VARCHAR(50),
#                 state VARCHAR(50),
#                 country VARCHAR(50),
#                 postcode INT,
#                 latitude VARCHAR(20),
#                 longitude VARCHAR(20),
#                 timezone_offset VARCHAR(10),
#                 timezone_description VARCHAR(50),
#                 email VARCHAR(100),
#                 uuid VARCHAR(100),
#                 username VARCHAR(50),
#                 password VARCHAR(50),
#                 salt VARCHAR(50),
#                 md5 VARCHAR(50),
#                 sha1 VARCHAR(50),
#                 sha256 VARCHAR(100),
#                 dob DATE,
#                 age INT,
#                 registered DATE,
#                 registered_age INT,
#                 phone VARCHAR(20),
#                 cell VARCHAR(20),
#                 picture_large VARCHAR(255),
#                 picture_medium VARCHAR(255),
#                 picture_thumbnail VARCHAR(255),
#                 nationality VARCHAR(5)
#             );
#             """

#             cursor.execute(create_table_query)
#             connection.commit()
#             print("Table created successfully")

#     except Error as e:
#         print(f"Error: {e}")

#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()

# # Call the function to create the table
# create_table()



import mysql.connector
from mysql.connector import Error
import requests

# Function to create the table (if it doesn't already exist)
def create_table():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='students',  # Replace with your database name
            user='root',               # Replace with your MySQL username
            password='Angel@1408'   # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            create_table_query = """
            CREATE TABLE IF NOT EXISTS user_info (
                gender VARCHAR(10),
                title VARCHAR(10),
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                street_number INT,
                street_name VARCHAR(100),
                city VARCHAR(50),
                state VARCHAR(50),
                country VARCHAR(50),
                postcode INT,
                latitude VARCHAR(20),
                longitude VARCHAR(20),
                timezone_offset VARCHAR(10),
                timezone_description VARCHAR(50),
                email VARCHAR(100),
                uuid VARCHAR(100),
                username VARCHAR(50),
                password VARCHAR(50),
                salt VARCHAR(50),
                md5 VARCHAR(50),
                sha1 VARCHAR(50),
                sha256 VARCHAR(100),
                dob DATE,
                age INT,
                registered DATE,
                registered_age INT,
                phone VARCHAR(20),
                cell VARCHAR(20),
                picture_large VARCHAR(255),
                picture_medium VARCHAR(255),
                picture_thumbnail VARCHAR(255),
                nationality VARCHAR(5)
            );
            """

            cursor.execute(create_table_query)
            connection.commit()
            print("Table created successfully")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to fetch data from Random User API
def fetch_data_from_api():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")
        return None

# Function to insert data into MySQL database
def insert_data(data):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='students',  # Replace with your database name
            user='root',               # Replace with your MySQL username
            password='Angel@1408'    # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            insert_query = """
            INSERT INTO user_info (
                gender, title, first_name, last_name, 
                street_number, street_name, city, state, country, postcode, 
                latitude, longitude, timezone_offset, timezone_description, 
                email, uuid, username, password, salt, md5, sha1, sha256, 
                dob, age, registered, registered_age, 
                phone, cell, picture_large, picture_medium, picture_thumbnail, nationality
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            for user in data['results']:
                user_data = (
                    user['gender'], user['name']['title'], user['name']['first'], user['name']['last'],
                    user['location']['street']['number'], user['location']['street']['name'], 
                    user['location']['city'], user['location']['state'], user['location']['country'], user['location']['postcode'],
                    user['location']['coordinates']['latitude'], user['location']['coordinates']['longitude'],
                    user['location']['timezone']['offset'], user['location']['timezone']['description'],
                    user['email'], user['login']['uuid'], user['login']['username'], user['login']['password'],
                    user['login']['salt'], user['login']['md5'], user['login']['sha1'], user['login']['sha256'],
                    user['dob']['date'], user['dob']['age'], user['registered']['date'], user['registered']['age'],
                    user['phone'], user['cell'], user['picture']['large'], user['picture']['medium'], user['picture']['thumbnail'], user['nat']
                )

                cursor.execute(insert_query, user_data)

            connection.commit()
            print("Data inserted successfully")

    except Error as e:
        print(f"Error while inserting data: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Create the table
create_table()

# Fetch data from API
api_data = fetch_data_from_api()

# Insert data into the table
if api_data:
    insert_data(api_data)

