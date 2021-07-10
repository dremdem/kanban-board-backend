"""Start task handler module."""
import http
import json
import logging

import task.actions as actions
import task.exceptions as tskexc


def start_task(data: dict) -> dict:
    """
    Start a task.

    :param data: Dictionary with the task name inside.
    :return: Dictionary with a HTTP status code and a message.
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
            actions.start_task(data['name'])
            body["message"] = f"Task {data['name']} started."
        except tskexc.TaskHTTPException as e:
            body = {"error": e.message}
            status_code = e.http_status
    return {"statusCode": status_code, "body": json.dumps(body)}


def start_task_handler(event, context):
    """
    Start task handler.

    :param event: All incoming info for an AWS Lambda function.
    :param context:
    :return: Dict with the response.
    """
    data = json.loads(event['body'])
    return start_task(data)


def get_elapsed_time(data: dict) -> dict:
    """
    Get elapsed time for a task.

    :param data: Dictionary with the task name inside.
    :return: Dictionary with a HTTP status code and a message.
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
            elapsed_time = actions.get_elapsed_time(data['name'])
            body["message"] = {"time": elapsed_time}
        except tskexc.TaskHTTPException as e:
            body = {"error": e.message}
            status_code = e.http_status
    return {"statusCode": status_code, "body": json.dumps(body)}


def get_elapsed_handler(event, context):
    """
    Get elapsed_time for a task handler.

    :param event: All incoming info for an AWS Lambda function.
    :param context:
    :return: Dict with the response.
    """
    data = json.loads(event['body'])
    return get_elapsed_time(data)
