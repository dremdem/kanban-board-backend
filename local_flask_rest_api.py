import json

from flask import Flask
from flask_restful import Resource, Api
import flask_restful.reqparse as reqparse

import task.new_task as new_task
import task.resolve_task as resolve_task
import task.start_task as start_task
import task.tasks as tasks


app = Flask(__name__)
api = Api(app)

task_name_parser = reqparse.RequestParser()
task_name_parser.add_argument("name", type=str, required=True)

get_tasks_parser = reqparse.RequestParser()
get_tasks_parser.add_argument("name", type=str, required=False)
get_tasks_parser.add_argument("status", type=str, required=False)
get_tasks_parser.add_argument("start_datetime", type=str, required=False)
get_tasks_parser.add_argument("end_datetime", type=str, required=False)


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


api.add_resource(ResolveTask, '/resolve')


class GetCost(Resource):
    def post(self):
        args = task_name_parser.parse_args()
        response = resolve_task.get_cost(args)
        return json.loads(response['body']), response['statusCode']


api.add_resource(GetCost, '/get_cost')


class GetTasks(Resource):
    def post(self):
        args = {k: v for k, v in get_tasks_parser.parse_args().items() if v}
        response = tasks.get_tasks(args)
        return json.loads(response['body']), response['statusCode']


api.add_resource(GetTasks, '/tasks')

if __name__ == '__main__':
    app.run(debug=True)
