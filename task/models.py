"""
Models for the tasks.

Import as:
import task.models as models
"""

import datetime as dt
import enum

import sqlalchemy as sqlal
import sqlalchemy.types as sqltypes

import db
import task.utils as utils


class TaskStatus(enum.Enum):
    """ Represents the task status(task location on a board). """
    todo = 1
    in_progress = 2
    done = 3


class Task(db.Base):
    """ The task itself """
    __tablename__ = "task"

    name = sqlal.Column(sqlal.String,
                        index=True,
                        primary_key=True,
                        comment="Task name")
    status = sqlal.Column(sqltypes.Enum(TaskStatus),
                          comment="Task status",
                          nullable=False)
    start_datetime = sqlal.Column(sqltypes.DateTime,
                                  comment="Start date and time of this task")
    end_datetime = sqlal.Column(sqltypes.DateTime,
                                comment="End date and time of this task")

    def to_dict(self):
        """
        Represents the task as a dict.

        :return: Dictionary with base task fields,
            and the calculation fields.
        """
        task = {
            "name": self.name,
            "status": str(self.status.name),
        }
        if self.start_datetime:
            task['start_datetime'] = self.start_datetime.isoformat()
            task['elapsed_time'] = utils.get_time_by_delta(
                (self.end_datetime or dt.datetime.now()) - self.start_datetime)
        if self.end_datetime:
            task['end_datetime'] = self.end_datetime.isoformat()
        if self.status == TaskStatus.done:
            task['cost'] = str(utils.get_cost_by_delta(
                self.end_datetime - self.start_datetime))
        return task

    def __repr__(self):
        """Task object representation."""
        return "<Task %r>" % self.name
