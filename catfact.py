import requests
import mysql.connector

# API URL
url = "https://catfact.ninja/fact"

# MySQL database connection setup
db_config = {
    'host': 'localhost',  # Replace with your MySQL server host (e.g., 'localhost')
    'user': 'root',       # Replace with your MySQL username
    'password': 'Angel@1408',  # Replace with your MySQL password
    'database': 'cat_facts_db'  # Replace with your database name
}

# Connect to MySQL database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cat_facts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        fact TEXT NOT NULL
    )
''')
conn.commit()

# Function to fetch cat facts from API
def fetch_cat_fact():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("fact", "No fact found")
    else:
        return None

# Fetch 50 facts and store them in the MySQL database
for _ in range(50):
    fact = fetch_cat_fact()
    if fact:
        cursor.execute("INSERT INTO cat_facts (fact) VALUES (%s)", (fact,))
        print("The fact of the day is : " , fact )
        conn.commit()  # Commit each fact to the database


# Close the connection to the database
cursor.close()
conn.close()

print("50 cat facts have been stored in the MySQL database.")
