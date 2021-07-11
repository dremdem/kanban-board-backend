"""
Utils for PostgreSQL DB.

Import as:

import db.utils as dbutils
"""

import sqlalchemy.orm as sqlorm

import db
import task.models as models


def wipe_tasks() -> None:
    """Delete all record from the Task table."""
    with sqlorm.Session(db.engine) as session:
        session.query(models.Task).delete()
        session.commit()

