
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route('/manager/<int:id>', methods=['DELETE'])
def del_manager(id):
    try:
        
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Angel@1408',
            database='employee_db'
        )
        
        
        cursor = connection.cursor()

        
        cursor.execute("SELECT * FROM employees WHERE id = %s", (id,))
        emp_data = cursor.fetchone()
        
        if emp_data:
            
            cursor.execute("DELETE FROM employees WHERE id = %s", (id,))
            connection.commit()
            return jsonify({"message": f"Employee data with ID {id} deleted successfully"}), 200
        else:
            
            return jsonify({"message": "User not found"}), 404
    
    except Error as e:
        
        return jsonify({"error": f"Error initializing database: {e}"}), 500
    
    finally:
        
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
