"""New task function handler module."""

import json
import logging

import task.actions as actions


def new_task(event: dict, context) -> dict:
    """
    New task handler.

    :param event: All incoming info for an AWS Lambda function.
    :param context:
    :return: Dict with the response.
    """
    data = json.loads(event['body'])
    if 'name' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
    print(data["name"])
    actions.add_task(data['name'])
    body = {
        "message": f"Task {data['name']} added.",
    }
    response = {"statusCode": 200, "body": json.dumps(body)}
    return response
