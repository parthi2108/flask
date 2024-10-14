from flask import Flask,request,jsonify
import mysql.connector
from mysql.connector import Error 

app = Flask(__name__)

# @app.route('/manager',methods=['GET'])


# def get_manager():
#     try: 
#         connection = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='Angel@1408',
#             database='employee_db'  
#         )
        
        # cursor = connection.cursor()
    
        
    #     cursor.execute ("Select * from employees")
    #     emp_date = cursor.fetchall()
    #     print("emp_data") 
        
    # except Error as e:
    #     print(f"error initialising database {e}")
        
    # finally :
    #     cursor.close()
    #     connection.close()
        
    #     return jsonify(emp_date)       
        
        
@app.route('/manager', methods=['POST'])

def postmanager():
    
    connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Angel@1408',
    database='employee_db'  
    )
        
    cursor = connection.cursor()
    try:   
        print(request.json)
        values = request.json
        insert_data = "INSERT INTO employees (id,name,age,position,phone_num),VALUES(%s,%s,%s,%s,%s)"
        data = (values['id'],values['name'],values['age'],values['position'],values['phone_num'])
        # data = (values 7,'parthiban',30,'developer',9363565443)
        print(values)
        cursor.execute ('insert_data','data')
        connection.commit()

    except Error as e:
        print(f"error initialising database {e}")
        
    finally :
        cursor.close()
        connection.close()
        
        return jsonify({"message":"Welcome manager"})   
            
if __name__ == '__main__':
   app.run(debug=True)