from flask import Flask 
from flask_restful import Api, Resource, reqparse

import pandas as pd

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        data = pd.read_csv('data.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('type', required=True)
        parser.add_argument('hp', required=True)
        args = parser.parse_args()

        data = pd.read_csv('data.csv')

        new_data = pd.DataFrame({
            'name'      : [args['name']],
            'type'       : [args['type']],
            'hp'      : [args['hp']]
        })

        data = data.append(new_data, ignore_index = True)
        data.to_csv('data.csv', index=False)
        return {'data' : new_data.to_dict('records')}, 201

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        args = parser.parse_args()

        data = pd.read_csv('/Resources/data.csv')

        data = data[data['name'] != args['name']]

        data.to_csv('data.csv', index=False)
        return {'message' : 'Record deleted successfully.'}, 200



# Add URL endpoints
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(debug=True)
