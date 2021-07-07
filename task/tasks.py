import json
import logging
import task.actions as actions


def get_tasks(event, context):
    data = json.loads(event['body'])
    if 'name' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't start the todo item.")
    print(data["name"])
    tasks = actions.get_tasks(data)
    body = {
        "message": f"Task {data['name']} added.",
        "tasks": json.dumps([task.to_dict() for task in tasks])
    }
    response = {"statusCode": 200, "body": json.dumps(body)}
    return response
