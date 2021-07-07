import dotenv
import sqlalchemy.orm as sqlorm
import sqlalchemy as sqlal
import os


dotenv.load_dotenv("db/postgres_config.env")

POSTGRES_CONN_STR = f"postgresql+psycopg2://" \
                    f"{os.environ.get('POSTGRES_USER')}:" \
                    f"{os.environ.get('POSTGRES_PASSWORD')}@" \
                    f"test_db/{os.environ.get('POSTGRES_DB')}"

print(POSTGRES_CONN_STR)

engine = sqlal.create_engine(POSTGRES_CONN_STR,
                             isolation_level="SERIALIZABLE")
session = sqlorm.Session(engine)
