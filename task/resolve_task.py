"""Resolve task handler module."""

import http
import json
import logging

import task.actions as actions
import task.exceptions as tskexc


def resolve_task(data: dict) -> dict:
    """
    Resolve task for the given name.

    :param data: Dictionary with the task name inside.
    :return: Dictionary with an HTTP status code and a message.
    """
    status_code = http.HTTPStatus.OK
    body = {"message": f"Task {data['name']} resolved."}
    if not data.get('name'):
        error_text = "Task name not entered."
        logging.error(error_text)
        status_code = http.HTTPStatus.BAD_REQUEST
        body = {"error": error_text}
    else:
        try:
            actions.resolve_task(data['name'])
        except tskexc.TaskHTTPException as e:
            body = {"error": e.message}
            status_code = e.http_status
    return {"statusCode": status_code, "body": json.dumps(body)}


def resolve_task_handler(event, context) -> dict:
    """
    Resolve task handler.

    :param event: All incoming info for an AWS Lambda function.
    :param context:
    :return: Dict with the response.
    """
    data = json.loads(event['body'])
    return resolve_task(data)


def get_cost(data: dict) -> dict:
    """
    Calculate the cost with the task name.

    :param data: Dictionary with the task name inside.
    :return: Dictionary with an HTTP status code and a message.
    """
    status_code = http.HTTPStatus.OK
    body = {}
    if not data.get('name'):
        error_text = "Task name not entered."
        logging.error(error_text)
        status_code = http.HTTPStatus.BAD_REQUEST
        body = {"error": error_text}
    else:
        try:
            cost = actions.get_cost(data['name'])
            body["message"] = {"cost": f"${cost}"}
        except tskexc.TaskHTTPException as e:
            body = {"error": e.message}
            status_code = e.http_status
    return {"statusCode": status_code, "body": json.dumps(body)}


def get_cost_handler(event, context) -> dict:
    """
    Get cost for task handler.

    :param event: All incoming info for an AWS Lambda function.
    :param context:
    :return: Dict with the response.
    """
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
