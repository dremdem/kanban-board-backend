"""
Business logic layer for the board.

Import as:

import task.actions as actions
"""

import datetime as dt
import decimal
import http
from typing import List, Dict

import sqlalchemy.orm.exc as sqlexc_orm
import sqlalchemy.orm as sqlorm
import sqlalchemy.exc as sqlexc
import db
import task.exceptions as tskexc
import task.models as models
import task.utils as utils


def validate_task_name(name: str) -> bool:
    """
    Make some validations for the task name.

    :param name: Task name.
    :return: Result of the validation.
    """
    # TODO(*): Add some tasks name validation.
    return True


def validate_filters(filters: Dict[str, str]) -> bool:
    """
    Validate conditions for the task request.

    :param filters: Dict representing conditions for the task model.
       Examples:
          {"name": "Plant a Tree"}
          {"status": "in_progress"}
          {"start_datetime": "2021-07-09 12:06:27.191299"}
    :return: Result of validation.
    """
    # TODO(*): Implement this validation.
    return True


def add_task(name: str) -> None:
    """
    Add a task by given name.

    :param name: Task name.
    """
    with sqlorm.Session(db.engine) as session:
        if not validate_task_name(name):
            raise tskexc.TaskHTTPException(http.HTTPStatus.BAD_REQUEST,
                                           "Task name %s is not valid." % name)
        new_task = models.Task(name=name, status=models.TaskStatus.todo)
        session.add(new_task)
        try:
            session.commit()
        except sqlexc.IntegrityError:
            raise tskexc.TaskHTTPException(
                http.HTTPStatus.CONFLICT,
                f"Task with the {name} name already exists.")


def start_task(name: str) -> None:
    """
    Start a task by given name.

    :param name: Task name.
    """
    with sqlorm.Session(db.engine) as session:
        try:
            task = session.query(models.Task). \
                filter(models.Task.name == name).one()
        except sqlexc_orm.NoResultFound:
            raise tskexc.TaskHTTPException(
                http.HTTPStatus.NOT_FOUND,
                f"There is no task: {name}")
        if task.status != models.TaskStatus.todo:
            raise tskexc.TaskHTTPException(
                http.HTTPStatus.CONFLICT,
                f"Task: {name} is not on the todo tab.")
        task.status = models.TaskStatus.in_progress
        task.start_datetime = dt.datetime.now()
        session.commit()


def resolve_task(name: str) -> None:
    """
    Resolve a task by given name.

    :param name: Task name.
    """
    with sqlorm.Session(db.engine) as session:
        try:
            task = session.query(models.Task). \
                filter(models.Task.name == name).one()
        except sqlexc.NoResultFound:
            raise Exception("There is no task: %s", name)
        if task.status != models.TaskStatus.in_progress:
            raise Exception("Task: %s is not in progress.")
        task.status = models.TaskStatus.done
        task.end_datetime = dt.datetime.now()
        session.commit()


def get_time_delta(task: models.Task) -> dt.timedelta:
    """
    Calculate the delta between task start time
     and the current time.

    :param task: Task name.
    :return: Datetime delta.
    """
    now = dt.datetime.now()
    return now - task.start_datetime


def get_elapsed_time(name: str) -> str:
    """
    Get elapsed_time for the certain task.

    :param name: Task name.
    :return: Elapsed time as string with the mask: <HH:MM:SS>
    """
    with sqlorm.Session(db.engine) as session:
        try:
            task = session.query(models.Task). \
                filter(models.Task.name == name).one()
        except sqlexc.NoResultFound:
            raise Exception("There is no task: %s", name)
        if task.status != models.TaskStatus.in_progress:
            raise Exception("Task: %s is not in progress.")
        delta = get_time_delta(task)
        return utils.get_time_by_delta(delta)


def get_cost(name: str) -> decimal.Decimal:
    """
    Calculate the cost for the given task.

    :param name: Task name.
    :return: Calculated cost.
    """
    with sqlorm.Session(db.engine) as session:
        try:
            task = session.query(models.Task). \
                filter(models.Task.name == name).one()
        except sqlexc.NoResultFound:
            raise Exception("There is no task: %s", name)
        if task.status != models.TaskStatus.done:
            raise Exception("Task: %s is not done.")
        delta = get_time_delta(task)
        return utils.get_cost_by_delta(delta)


def get_tasks(filters: dict) -> List[models.Task]:
    """
    Get tasks for the given filters.

    :param filters: Dictionary with the filters.
        Examples:
          {"name": "Plant a Tree"}
          {"status": "in_progress"}
          {"start_datetime": "2021-07-09 12:06:27.191299"}
    :return:
    """
    if not validate_filters(filters):
        raise Exception("Filters validation failed.")
    with sqlorm.Session(db.engine) as session:
        # RFE(*): Have to handle partially entered dates like "2021-07-09"
        return session.query(models.Task).filter_by(**filters)
