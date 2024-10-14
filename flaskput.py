from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Correct route with <int:id> to capture employee ID in the URL
@app.route('/manager/<int:id>', methods=['GET','PUT'])
def update_manager(id):
    try:
        # Connecting to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Angel@1408',
            database='employee_db'
        )
        
        cursor = connection.cursor()
        
        # Fetching the data from the request
        data = request.get_json()
        new_name = data.get('name')
        new_age = data.get('age')
        new_position = data.get('position')
        new_phone_num = data.get('phone_num')
        
        # Checking if the employee exists in the database
        cursor.execute("SELECT * FROM employees WHERE id = %s", (id,))
        emp_data = cursor.fetchone()

        if emp_data:
            # Updating the employee record if found
            cursor.execute("""
                UPDATE employees 
                SET name = %s, age = %s, position = %s, phone_num = %s 
                WHERE id = %s
            """, (new_name, new_age, new_position, new_phone_num, id))
            connection.commit()
            
            return jsonify({"message": f"Employee data with ID {id} updated successfully"}), 200
        else:
            # If no employee is found with the given ID
            return jsonify({"message": "Employee not found"}), 404
    
    except Error as e:
        # Handling database connection or query errors
        return jsonify({"error": f"Error initializing database: {e}"}), 500
    
    finally:
        # Ensuring the cursor and connection are properly closed
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
