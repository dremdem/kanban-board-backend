import http

from flask import Flask
from flask_restful import Resource, Api
import flask_restful.reqparse as reqparse

import task.new_task as new_task

app = Flask(__name__)
api = Api(app)

new_task_parser = reqparse.RequestParser()
new_task_parser.add_argument("name", type=str)


class NewTask(Resource):
    def post(self):
        args = new_task_parser.parse_args()
        response = new_task.new_task(args)
        return response['body'], response['statusCode']


api.add_resource(NewTask, '/new')

if __name__ == '__main__':
    app.run(debug=True)
