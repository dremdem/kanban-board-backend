"""
Provide all credentials for PostgreSQL DB.

Import as:
import db
"""

import os

import dotenv
import sqlalchemy as sqlal
import sqlalchemy.orm as sqlorm

dotenv.load_dotenv("db/postgres_config.env")
POSTGRES_CONN_STR = f"postgresql+psycopg2://" \
                    f"{os.environ.get('POSTGRES_USER')}:" \
                    f"{os.environ.get('POSTGRES_PASSWORD')}@" \
                    f"{os.environ.get('POSTGRES_HOST')}/{os.environ.get('POSTGRES_DB')}"
engine = sqlal.create_engine(POSTGRES_CONN_STR,
                             isolation_level="SERIALIZABLE")
Base = sqlorm.declarative_base()
