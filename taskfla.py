from flask import Flask,request,jsonify
import mysql.connector 
from mysql.connector import error 

app = Flask(__name__)

@app.route('\ update_address', methods=['POST'])

def update_address():
    
    try:
        connection = mysql.connector.connect(
            host = 'localhost'
            user = 'root'
            password = 'Angel@1408'
            database = 'students'
        )
        
        cursor=connection.cursor()

        query = 'UPDATE student_address_transportation SET address = %s WHERE RollNo = %s'
        values = '"oppanakara_street",2'
        cursor.execute(query,values)
        
        connection.commit     
        
    return jsonify({"error":str(e)}), 500 
        
    
    