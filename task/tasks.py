"""Get tasks handler module."""

import http
import json

import task.actions as actions
import task.exceptions as tskexc


def get_tasks_handler(event, context) -> dict:
    """
    Get tasks handler.

    :param event: All incoming info for an AWS Lambda function.
    :param context:
    :return: Dict with the response.
    """
    data = json.loads(event['body'])
    return get_tasks(data)


def get_tasks(data: dict) -> dict:
    """
    Get tasks with the dict filters.

    :param data: Dictionary with the filters.
        Examples:
          {"name": "Plant a Tree"}
          {"status": "in_progress"}
          {"start_datetime": "2021-07-09 12:06:27.191299"}
    :return: Dictionary with an HTTP status code and a message.
    """
    status_code = http.HTTPStatus.OK
    body = {"filters": data}
    try:
        tasks = actions.get_tasks(data)
        body["tasks"] = [task.to_dict() for task in tasks]
    except tskexc.TaskHTTPException as e:
        body = {"error": e.message}
        status_code = e.http_status
    return {"statusCode": status_code, "body": json.dumps(body)}
