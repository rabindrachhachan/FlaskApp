#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_restful import Api, Resource, reqparse, fields, marshal
from flaskext.mysql import MySQL
import json
import collections
from bson import json_util
import datetime
from time import mktime






mysql = MySQL()


app = Flask(__name__)
api = Api(app)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)
  
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'forget'
app.config['MYSQL_DATABASE_DB'] = 'employees'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


#Retrieve all record
class MyEncoder(json.JSONEncoder):

    def default(self, row):
        if isinstance(row, datetime.datetime):
            return row.__str__()

        

class GetAllRecord(Resource):
    def get(self):
        try: 
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=str)
            parser.add_argument('expense_date', type=str)
            parser.add_argument('expense_category', type=str)
            parser.add_argument('type', type=str)
            parser.add_argument('amount', type=str)
            args = parser.parse_args()

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT ID,Expense_Date,Expense_category,Type,Amount FROM expense")
            # fetch all of the rows from the query
            row = cursor.fetchall()
            conn.commit()
            return {'StatusCode':'200','Message': 'Success'}

        except Exception as e:
             return {'error': str(e)}
    
      
#Retrieve a specific record               
class GetRecord(Resource):
    def get(self):
        try: 
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=str)
            args = parser.parse_args()
           

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT ID,Expense_Date,Expense_category,Type,Amount FROM expense where ID=id")
            data = cursor.fetchall()

            conn.commit()
            return {'StatusCode':'200','Message': 'Success'}

        except Exception as e:
             return {'error': str(e)}
            
#Create a new record
class AddRecord(Resource):
  def post(self):
        try: 
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=str)
            parser.add_argument('expense_date', type=str)
            parser.add_argument('expense_category', type=str)
            parser.add_argument('type', type=str)
            parser.add_argument('amount', type=str)
            
            args = parser.parse_args()

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO  expense(ID,Expense_Date,Expense_category,Type,Amount ) VALUES ( id,expense_date,expense_category,type,amount )")

            conn.commit()
            return {'StatusCode':'200','Message': 'Success'}

        except Exception as e:
             return {'error': str(e)}
            
#Update a existing record
class UpdateRecord(Resource):
    def put(self):
        try: 
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=str)
            parser.add_argument('amount', type=str)
            args = parser.parse_args()
           
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("UPDATE expense set Amount=amount where ID=id")
            conn.commit()
            return {'StatusCode':'200','Message': 'Success'}

        except Exception as e:
             return {'error': str(e)}
            
#Delete a record
class DeleteRecord(Resource):
    def delete(self):
        try: 
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=str)
            args = parser.parse_args()
          
      

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("DELETE from expense  where ID=id")
            data = cursor.fetchall()

            conn.commit()
            return {'StatusCode':'200','Message': 'Success'}

        except Exception as e:
             return {'error': str(e)}

            
api.add_resource(GetAllRecord, '/GetAllRecord')
api.add_resource(GetRecord, '/GetRecord')
api.add_resource(AddRecord, '/AddRecord')
api.add_resource(UpdateRecord, '/UpdateRecord')
api.add_resource(DeleteRecord, '/DeleteRecord')           


if __name__ == '__main__':
 app.run(debug=True)
