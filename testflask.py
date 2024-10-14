from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error


app = Flask(__name__)

@app.route('/manager',methods=['GET'])
def getmanager():
    connection = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="Angel@1408"  
        )
    cursor = connection.cursor()
    try:
        cursor.execute("USE employee_db")
        cursor.execute("select * from employees")
        empData = cursor.fetchall()
        print(empData)
    except Error as e:
        print(f"Error initializing database: {e}")
    finally:
        cursor.close()
        connection.close()
    return jsonify(empData)

@app.route('/manager',methods=['POST'])
def postmanager():
    connection = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="Angel@1408" 
        )
    cursor = connection.cursor()
    try:
        print(request.json)
        values = request.json
        cursor.execute("USE employee_db")
        insert_data = "INSERT INTO employees (id, name, age, position, phone_num) VALUES (%s,%s,%s,%s,%s)"
        data = (values['id'], values['name'], values['age'], values['position'], values['phone_num'])
        cursor.execute(insert_data,data)
        connection.commit()
    except Error as e:
        print(f"Error initializing database: {e}")
    finally:
        cursor.close()
        connection.close()
    return jsonify({"message":"Inserted Sucessfully"})

if __name__ == '__main__':
    app.run(debug=True)