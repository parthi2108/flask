# from flask import Flask,request,jsonify
# import mysql.connector
# from mysql.connector import Error 
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask app is running!"

if __name__ == '__main__':
    app.run(debug=True, )

# app=Flask(__name__)

# @app.route('/task1',methods=['GET'])

# def update_manager():
    
#     try:
#         connection=mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='Angel@1408',
#             database='parthi_db1'
#         )
    
#         cursor = connection.cursor()
#         cursor.execute ("select * from task1")
#         emp_data = cursor.fetchall()
#         print("emp_data")
        
#     except Error as e:
#         print(f"error initialising database {e}")
        
#     finally :
#         cursor.close()
#         connection.close()
#         return jsonify(emp_data)
    
# if __name__ == '__main__':
#     app.run(debug=True)
    
        
    
    