# from flask import Flask , request, jsonify
# import mysql.connector
# from mysql.connector import Error 

# app=Flask(__name__)

# @app.route('/update_address' , methods=['POST'])

# def update_address():
    
#     try:
    
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root", 
#             password="Angel@1408",
#             database="students"  
#         )

#         cursor = connection.cursor()
#         cursor.execute("use students")
#         cursor.execute('update student_address_transportation set address="%s" where RollNo=%s')
        

#         empData = cursor.fetchall()
        
#         return jsonify(empData)
    
#     except Error as e:
#       return jsonify("error",e), 500
  
#     finally:
#       if cursor:    
#         cursor.close()
#       if connection:
#         connection.close()

# # if __name__ == '__main__':

# #   app.run(debug=True)
        
        
# @app.route('/update_address' , methods=['GET'])

# def print_db():
    
#     try:
    
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root", 
#             password="Angel@1408",
#             database="students"  
#         )

#         cursor = connection.cursor()
#         cursor.execute("use students")
#         cursor.execute('select * from students')


#         empData = cursor.fetchall()
        
#         return jsonify(empData)
    
#     except Error as e:
#       return jsonify("error",e), 500
  
#     finally:
#       if cursor:    
#         cursor.close()
#       if connection:
#         connection.close()

# if __name__ == '__main__':

#   app.run(debug=True)


from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error 

app = Flask(__name__)

# Route to update address in the database
@app.route('/update_address', methods=['POST'])
def update_address():
    try:
        # Establish the database connection
        connection = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="Angel@1408",
            database="students"  
        )

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Update query to change the address
        query = 'UPDATE student_address_transportation SET address = %s WHERE RollNo = %s'
        values = ("Oppanakara street", 2)
        cursor.execute(query, values)

        # Commit the changes
        connection.commit()

        return jsonify({"message": "Address updated successfully!"}), 200

    except Error as e:
        return jsonify({"error": str(e)}), 500
  
    finally:
        # Ensure the cursor and connection are closed properly
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Route to fetch and display all data
@app.route('/get_data', methods=['GET'])
def print_db():
    try:
        # Establish the database connection
        connection = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="Angel@1408",
            database="students"  
        )

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Query to fetch all data from the student_address_transportation table
        cursor.execute('SELECT * FROM student_address_transportation')

        # Fetch all rows from the table
        empData = cursor.fetchall()

        return jsonify(empData), 200
    
    except Error as e:
        return jsonify({"error": str(e)}), 500
  
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Only one app.run() is needed
if __name__ == '__main__':
    app.run(debug=True)
