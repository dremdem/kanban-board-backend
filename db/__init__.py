"""
Provide all credentials for PostgreSQL DB.

Import as:
import db
"""

import os

import dotenv
import sqlalchemy as sqlal
import sqlalchemy.orm as sqlorm

KANBAN_BOARD_STAGE = os.environ.get('KANBAN_BOARD_STAGE', 'prod')
dotenv.load_dotenv(os.path.join(os.path.dirname(__file__),
                                f"{KANBAN_BOARD_STAGE}_postgres_config.env"))
POSTGRES_CONN_STR = f"postgresql+psycopg2://" \
                    f"{os.environ.get('POSTGRES_USER')}:" \
                    f"{os.environ.get('POSTGRES_PASSWORD')}@" \
                    f"{os.environ.get('POSTGRES_HOST')}/{os.environ.get('POSTGRES_DB')}"
engine = sqlal.create_engine(POSTGRES_CONN_STR,
                             isolation_level="SERIALIZABLE")
Base = sqlorm.declarative_base()
