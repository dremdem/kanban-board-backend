import enum
import sqlalchemy as sqlal
import sqlalchemy.orm as sqlorm
import datetime as dt
import sqlalchemy.types as sqltypes
import task.actions as actions

HOURLY_RATE = 10

Base = sqlorm.declarative_base()


class TaskStatus(enum.Enum):
    todo = 1
    in_progress = 2
    done = 3


class Task(Base):
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
        task = {
            "name": self.name,
            "status": str(self.status.name),
        }
        if self.start_datetime:
            task['start_datetime'] = self.start_datetime.isoformat()
            task['elapsed_time'] = actions.get_time_by_delta(
                (self.end_datetime or dt.datetime.now()) - self.start_datetime)
        if self.end_datetime:
            task['end_datetime'] = self.end_datetime.isoformat()
        if self.status == TaskStatus.done:
            task['cost'] = str(actions.get_cost_by_delta(
                self.end_datetime - self.start_datetime))
        return task

    def __repr__(self):
        return "<Task %r>" % self.name
