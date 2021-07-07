import task.models as models
import sqlalchemy.orm.exc as sqlexc
import sqlalchemy.orm as sqlorm
import decimal
from typing import List, Dict
import db
import datetime as dt


def validate_task_name(name: str) -> bool:
    # TODO(*): Add some tasks name validation.
    return True


def add_task(name: str) -> None:
    if not validate_task_name(name):
        Exception("Task name %s is not valid." % name)

    new_task = models.Task(name=name, status=models.TaskStatus.todo)
    db.session.add(new_task)
    db.session.flush()
    db.session.commit()


def start_task(name: str) -> None:
    try:
        task = db.session.query(models.Task). \
            filter(models.Task.name == name).one()
    except sqlexc.NoResultFound:
        raise Exception("There is no task: %s", name)
    if task.status != models.TaskStatus.todo:
        raise Exception("Task: %s is not on the todo tab.")
    task.status = models.TaskStatus.in_progress
    task.start_datetime = dt.datetime.now()
    db.session.commit()


def resolve_task(name: str) -> None:
    try:
        task = db.session.query(models.Task). \
            filter(models.Task.name == name).one()
    except sqlexc.NoResultFound:
        raise Exception("There is no task: %s", name)
    if task.status != models.TaskStatus.in_progress:
        raise Exception("Task: %s is not in progress.")
    task.status = models.TaskStatus.done
    task.end_datetime = dt.datetime.now()
    db.session.commit()


def get_time_delta(task: models.Task) -> dt.timedelta:
    now = dt.datetime.now()
    return now - task.start_datetime


def get_time_by_delta(delta: dt.timedelta) -> str:
    days, seconds = delta.days, delta.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return "%02d:%02d:%02d" % (hours, minutes, seconds)


def get_elapsed_time(name: str) -> str:
    with sqlorm.Session(db.engine) as session:
        try:
            task = session.query(models.Task). \
                filter(models.Task.name == name).one()
        except sqlexc.NoResultFound:
            raise Exception("There is no task: %s", name)
        if task.status != models.TaskStatus.in_progress:
            raise Exception("Task: %s is not in progress.")
        delta = get_time_delta(task)
        return get_time_by_delta(delta)


def get_cost_by_delta(delta: dt.timedelta) -> decimal.Decimal:
    hours = delta.seconds / 60 / 60
    decimal.getcontext().prec = 3
    return decimal.Decimal(hours) * decimal.Decimal(models.HOURLY_RATE)


def get_cost(name: str) -> decimal.Decimal:
    with sqlorm.Session(db.engine) as session:
        try:
            task = session.query(models.Task). \
                filter(models.Task.name == name).one()
        except sqlexc.NoResultFound:
            raise Exception("There is no task: %s", name)
        if task.status != models.TaskStatus.done:
            raise Exception("Task: %s is not done.")
        delta = get_time_delta(task)
        return get_cost_by_delta(delta)


def validate_filters(filters: Dict[str, str]) -> bool:
    # TODO(*): Implement this validation.
    return True


def get_tasks(filters: dict) -> List[models.Task]:
    if not validate_filters(filters):
        raise Exception("Filters validation failed.")
    with sqlorm.Session(db.engine) as session:
        return session.query(models.Task).filter_by(**filters)
