# import mysql.connector

# # MySQL database connection setup
# db_config = {
#     'host': 'localhost',  # Replace with your MySQL server host (e.g., 'localhost')
#     'user': 'root',       # Replace with your MySQL username
#     'password': 'Angel@1408',  # Replace with your MySQL password
#     'database': 'employee_db'  # Database name
# }

# # Connect to MySQL server (without specifying the database, to create it if needed)
# conn = mysql.connector.connect(
#     host=db_config['host'],
#     user=db_config['user'],
#     password=db_config['password']
# )
# cursor = conn.cursor()

# # Create the database if it doesn't exist
# cursor.execute("CREATE DATABASE IF NOT EXISTS employee_db")
# conn.commit()

# # Now connect to the specific database
# conn = mysql.connector.connect(**db_config)
# cursor = conn.cursor()

# # Create table if it doesn't exist
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS employees (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(255) NOT NULL,
#         age INT NOT NULL,
#         position VARCHAR(255) NOT NULL
#     )
# ''')
# conn.commit()

# # CREATE: Add a new employee to the database
# def create_employee(name, age, position):
#     query = "INSERT INTO employees (name, age, position) VALUES (%s, %s, %s)"
#     cursor.execute(query, (name, age, position))
#     conn.commit()
#     print(f"Employee {name} added.")

# # READ: Retrieve all employees from the database
# def read_employees():
#     query = "SELECT * FROM employees"
#     cursor.execute(query)
#     result = cursor.fetchall()
#     for row in result:
#         print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Position: {row[3]}")

# # UPDATE: Update an employee's details
# def update_employee(employee_id, name=None, age=None, position=None):
#     query = "UPDATE employees SET "
#     fields = []
#     values = []

#     if name:
#         fields.append("name = %s")
#         values.append(name)
#     if age:
#         fields.append("age = %s")
#         values.append(age)
#     if position:
#         fields.append("position = %s")
#         values.append(position)

#     query += ", ".join(fields) + " WHERE id = %s"
#     values.append(employee_id)

#     cursor.execute(query, values)
#     conn.commit()
#     print(f"Employee with ID {employee_id} updated.")

# # DELETE: Remove an employee from the database
# def delete_employee(employee_id):
#     query = "DELETE FROM employees WHERE id = %s"
#     cursor.execute(query, (employee_id,))
#     conn.commit()
#     print(f"Employee with ID {employee_id} deleted.")

# # User input to demonstrate the CRUD operations
# while True:
#     print("\n--- Employee Management ---")
#     print("1. Add Employee")
#     print("2. View Employees")
#     print("3. Update Employee")
#     print("4. Delete Employee")
#     print("5. Exit")

#     choice = input("Enter your choice (1-5): ")

#     if choice == '1':
#         name = input("Enter name: ")
#         age = int(input("Enter age: "))
#         position = input("Enter position: ")
#         create_employee(name, age, position)
    
#     elif choice == '2':
#         print("\nEmployee List:")
#         read_employees()
    
#     elif choice == '3':
#         employee_id = int(input("Enter employee ID to update: "))
#         name = input("Enter new name (leave blank to skip): ") or None
#         age = input("Enter new age (leave blank to skip): ")
#         age = int(age) if age else None
#         position = input("Enter new position (leave blank to skip): ") or None
#         update_employee(employee_id, name, age, position)
    
#     elif choice == '4':
#         employee_id = int(input("Enter employee ID to delete: "))
#         delete_employee(employee_id)
    
#     elif choice == '5':
#         print("Exiting...")
#         break
    
#     else:
#         print("Invalid choice. Please try again.")

# # Close the database connection
# cursor.close()
# conn.close()



import mysql.connector

# MySQL database connection setup
db_config = {
    'host': 'localhost',  # Replace with your MySQL server host (e.g., 'localhost')
    'user': 'root',       # Replace with your MySQL username
    'password': 'Angel@1408',  # Replace with your MySQL password
    'database': 'employee_db'  # Database name
}

# Connect to MySQL server and database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Check if the 'phone_num' column exists, and if not, add it
cursor.execute("SHOW COLUMNS FROM employees LIKE 'phone_num'")
result = cursor.fetchone()

if not result:
    cursor.execute('''
        ALTER TABLE employees 
        ADD COLUMN phone_num VARCHAR(10)
    ''')
    conn.commit()

# CREATE: Add a new employee to the database
def create_employee(name, age, position, phone_num):
    if validate_phone(phone_num):
        query = "INSERT INTO employees (name, age, position, phone_num) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, age, position, phone_num))
        conn.commit()
        print(f"Employee {name} added with phone number {phone_num}.")
    else:
        print(f"Invalid phone number {phone_num}. Please enter a valid 10-digit phone number starting with 9, 8, 7, or 6.")

# READ: Retrieve all employees from the database
def read_employees():
    query = "SELECT * FROM employees"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Position: {row[3]}, Phone Number: {row[4]}")

# UPDATE: Update an employee's details
def update_employee(employee_id, name=None, age=None, position=None, phone_num=None):
    query = "UPDATE employees SET "
    fields = []
    values = []

    if name:
        fields.append("name = %s")
        values.append(name)
    if age:
        fields.append("age = %s")
        values.append(age)
    if position:
        fields.append("position = %s")
        values.append(position)
    if phone_num:
        if validate_phone(phone_num):
            fields.append("phone_num = %s")
            values.append(phone_num)
        else:
            print(f"Invalid phone number {phone_num}.")
            return

    query += ", ".join(fields) + " WHERE id = %s"
    values.append(employee_id)

    cursor.execute(query, values)
    conn.commit()
    print(f"Employee with ID {employee_id} updated.")

# DELETE: Remove an employee from the database
def delete_employee(employee_id):
    query = "DELETE FROM employees WHERE id = %s"
    cursor.execute(query, (employee_id,))
    conn.commit()
    print(f"Employee with ID {employee_id} deleted.")

# Phone number validation
def validate_phone(phone_num):
    if len(phone_num) == 10 and phone_num[0] in '9876':
        return True
    else:
        return False

# User input to demonstrate the CRUD operations
while True:
    print("\n--- Employee Management ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        position = input("Enter position: ")
        phone_num = input("Enter phone number: ")

        create_employee(name, age, position, phone_num)
    
    elif choice == '2':
        print("\nEmployee List:")
        read_employees()
    
    elif choice == '3':
        employee_id = int(input("Enter employee ID to update: "))
        name = input("Enter new name (leave blank to skip): ") or None
        age = input("Enter new age (leave blank to skip): ")
        age = int(age) if age else None
        position = input("Enter new position (leave blank to skip): ") or None
        phone_num = input("Enter new phone number (leave blank to skip): ") or None
        update_employee(employee_id, name, age, position, phone_num)
    
    elif choice == '4':
        employee_id = int(input("Enter employee ID to delete: "))
        delete_employee(employee_id)
    
    elif choice == '5':
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
cursor.close()
conn.close()
