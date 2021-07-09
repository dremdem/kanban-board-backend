"""New task function handler module."""
import http
import json
import logging

import task.actions as actions
import task.exceptions as tskexc


def new_task(data: dict) -> dict:
    status_code = http.HTTPStatus.CREATED
    body = {}
    if 'name' not in data:
        error_text = "Task name not entered."
        logging.error(error_text)
        status_code = http.HTTPStatus.BAD_REQUEST
        body = {"error": error_text}
    else:
        try:
            actions.add_task(data['name'])
            body["message"] = f"Task {data['name']} added."
        except tskexc.TaskHTTPException as e:
            body = {"error": e.message}
            status_code = e.http_status
    return {"statusCode": status_code, "body": json.dumps(body)}


def new_task_handler(event: dict, context) -> dict:
    """
    New task handler.

    :param event: All incoming info for an AWS Lambda function.
    :param context:
    :return: Dict with the response.
    """
    data = json.loads(event['body'])
    return new_task(data)
