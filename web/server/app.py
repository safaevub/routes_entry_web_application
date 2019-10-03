from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api, Resource
from pymongo import MongoClient
from bson import json_util
import os
import json
import uuid

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017/routes")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert(
{
    'objectType':'user',
    'id': uuid.uuid4().hex,
    'location': "Lillehammer",
    'date': '15/09/2019',
    'geo': "lat: 123 long: 345",
    'routename': 'Jack Kerouac',
    'grade': "6+",
    'length': '12'
})
UserNum.insert(
{
    'objectType':'user',
    'id': uuid.uuid4().hex,
    'location': "Gjovik",
    'date': '13/09/2019',
    'geo': "lat: 13 long: 545",
    'routename': 'Lofoten',
    'grade': "9+",
    'length': '14'
})
UserNum.insert(
{
    'objectType':'user',
    'id': uuid.uuid4().hex,
    'location': "Lillehammer",
    'date': '15/09/2019',
    'geo': "lat: 123 long: 345",
    'routename': 'Jack Kerouac',
    'grade': "6+",
    'length': "12"
})
UserNum.insert(
{
    'objectType':'user',
    'id': uuid.uuid4().hex,
    'location': "Gjovik",
    'date': '13/09/2019',
    'geo': "lat: 13 long: 545",
    'routename': 'Hell Kitchen',
    'grade': "9+",
    'length': "14"
})
UserNum.insert(
{
    'objectType':'user',
    'id': uuid.uuid4().hex,
    'location': "Oslo",
    'date': '11/09/2019',
    'geo': "lat 3423 long 3455",
    'routename': 'Heaven',
    'grade': "7+",
    'length': "129"
})

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
class Visit(Resource):
    def get(self):
        documents = []
        for c in UserNum.find({'objectType':'user'}):
            c.pop("_id")
            documents.append(c)
        return jsonify(documents)

@app.route('/routes', methods=['GET', 'POST'])
def all_routes():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        UserNum.insert({
            'objectType':'user',
            'id': uuid.uuid4().hex,
            'location': post_data.get('location'),
            'date': post_data.get('date'),
            'geo': post_data.get('geo'),
            'routename': post_data.get('routename'),
            'grade' : post_data.get('grade'),
            'length' : post_data.get('length')
        })
        response_object['message'] = 'Route added!'
    else:
        documents = []
        for c in UserNum.find({'objectType':'user'}):
            c.pop("_id")
            documents.append(c)

        response_object['routes'] = documents

    return jsonify(response_object)

@app.route('/routes/<route_id>', methods=['PUT', 'DELETE'])
def single_route(route_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_route(route_id)
        UserNum.insert({
            'objectType':'user',
            'id': uuid.uuid4().hex,
            'location': post_data.get('location'),
            'date': post_data.get('date'),
            'geo': post_data.get('geo'),
            'routename': post_data.get('routename'),
            'grade' : post_data.get('grade'),
            'length' : post_data.get('length')
        })
        response_object['message'] = 'Route updated!'
    if request.method == 'DELETE':
        remove_route(route_id)
        response_object['message'] = 'Route removed!'
    return jsonify(response_object)
def remove_route(route_id):
    which_one = {"id": route_id}
    UserNum.delete_one(which_one)
    return True

api.add_resource(Visit,"/newhello")



if __name__ == '__main__':
    app.run(host="0.0.0.0")
