import json
import logging
import task.actions as actions


def resolve_task(event, context):
    data = json.loads(event['body'])
    if 'name' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't start the todo item.")
    print(data["name"])
    actions.resolve_task(data['name'])
    body = {
        "message": f"Task {data['name']} added.",
    }
    response = {"statusCode": 200, "body": json.dumps(body)}
    return response


def get_cost(event, context):
    data = json.loads(event['body'])
    if 'name' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't start the todo item.")
    print(data["name"])
    cost = actions.get_cost(data['name'])
    body = {
        "message": {"cost": f"${cost}"},
    }
    response = {"statusCode": 200, "body": json.dumps(body)}
    return response
