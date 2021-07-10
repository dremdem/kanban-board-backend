import http

import json
from flask import Flask
from flask_restful import Resource, Api
import flask_restful.reqparse as reqparse

import task.new_task as new_task
import task.start_task as start_task
import task.resolve_task as resolve_task

app = Flask(__name__)
api = Api(app)

task_name_parser = reqparse.RequestParser()
task_name_parser.add_argument("name", type=str)


class NewTask(Resource):
    def post(self):
        args = task_name_parser.parse_args()
        response = new_task.new_task(args)
        return json.loads(response['body']), response['statusCode']


api.add_resource(NewTask, '/new')


class StartTask(Resource):
    def post(self):
        args = task_name_parser.parse_args()
        response = start_task.start_task(args)
        return json.loads(response['body']), response['statusCode']


api.add_resource(StartTask, '/start')


class GetElapsedTime(Resource):
    def post(self):
        args = task_name_parser.parse_args()
        response = start_task.get_elapsed_time(args)
        return json.loads(response['body']), response['statusCode']


api.add_resource(GetElapsedTime, '/get_elapsed_time')


class ResolveTask(Resource):
    def post(self):
        args = task_name_parser.parse_args()
        response = resolve_task.resolve_task(args)
        return json.loads(response['body']), response['statusCode']


api.add_resource(ResolveTask, '/resolve_task')

if __name__ == '__main__':
    app.run(debug=True)
