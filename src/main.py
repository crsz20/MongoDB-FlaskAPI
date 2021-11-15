import os
from dotenv import load_dotenv

import pymongo

from flask import Flask, request, Response
from flask_cors import CORS
from flask_restful import Resource, Api

import json
from bson import ObjectId

app = Flask(__name__)
CORS(app)

print('\n')

# Connect Python to the database
try:
    load_dotenv()
    MONGO_CLUSTER = os.environ['MONGO_URI']
    client = pymongo.MongoClient(MONGO_CLUSTER)
    # client = pymongo.MongoClient(MONGO_URI)

    db = client.hackathon
    users = db.users
    
except Exception:
    print("Error connecting...")


print('\n')


########################## Sample Query ##########################
#search = users.find_one({'name': 'Jerry'})
# pprint(search)
# print(search.get('name'))


########################## Vanilla Flask ##########################

# login endpoint handle login requests
# @app.route('/login', methods=["POST", "GET"])
# def login():
#     if (request.method == "POST"):
#         data = request.get_json()
#         print(data)
#         res = users.find_one({"name": data['name']})
#         print(res)

#         # return information for user
#         return {
#             "name": res['name'],
#             "trade_his": res['trade_hist'],
#             "holdings": res['holdings']
#         }
#     return "you made a GET request failure"


# @app.route("/", methods=["POST", "GET"])
# def index():
#     if (request.method == "POST"):
#         doc = request.get_json()
#         print(doc)
#         users.insert_one(doc)
#         return "what in the world are you doing?"
#     else:
#         return "Why did you GET?\nLet's GET this bread!"
    

# @app.route("/query/<string:name>", methods=["GET"])
# def query(name):
#     search = users.find_one({'name': name})
#     print(search)
#     return Response(json.dumps(search,default=str),mimetype="application/json")


########################## Flask RESTful ##########################

class Landing(Resource):
    def get(self):
        return {'info': 'hi there'}

class Query(Resource):
    def get(self,name):
        search = users.find_one({'name': name})
        print(search)
        return Response(json.dumps(search,default=str),mimetype="application/json")

class Login(Resource):
    def post(self):
        if (request.method == "POST"):
            data = request.get_json()
            print(data)
            res = users.find_one({"name": data['name']})
            print(res)

            # return information for user
            return {
                "name": res['name'],
                "trade_his": res['trade_hist'],
                "holdings": res['holdings']
            }
    
    def get(self):
        return "you made a GET request failure"

    


api = Api(app)
api.add_resource(Landing, '/')
api.add_resource(Query, '/query/<string:name>')    
api.add_resource(Login, '/login')



if __name__ == '__main__':
    # with debug enabled, the server will reload itself when the code changes
    app.run(debug=True)

# import flask_restful may be cleaner