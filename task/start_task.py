import json
import logging
import task.actions as actions


def start_task(event, context):
    data = json.loads(event['body'])
    if 'name' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't start the todo item.")
    print(data["name"])
    actions.start_task(data['name'])
    body = {
        "message": f"Task {data['name']} added.",
    }
    response = {"statusCode": 200, "body": json.dumps(body)}
    return response


def get_elapsed_time(event, context):
    data = json.loads(event['body'])
    if 'name' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't start the todo item.")
    print(data["name"])
    elapsed_time = actions.get_elapsed_time(data['name'])
    body = {
        "message": {"time": elapsed_time},
    }
    response = {"statusCode": 200, "body": json.dumps(body)}
    return response
