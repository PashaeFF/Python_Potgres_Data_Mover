from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

POSTGRES_DB_LOAD = os.getenv("POSTGRES_DB_LOAD")
POSTGRES_USER_LOAD = os.getenv("POSTGRES_USER_LOAD")
POSTGRES_PASSWORD_LOAD = os.getenv("POSTGRES_PASSWORD_LOAD")
POSTGRES_HOST_LOAD = os.getenv("POSTGRES_HOST_LOAD")
POSTGRES_PORT_LOAD = os.getenv("POSTGRES_PORT_LOAD")


input_file = "backup_postgresql.sql"

connection = psycopg2.connect(
            database=POSTGRES_DB_LOAD,
            user=POSTGRES_USER_LOAD,
            password=POSTGRES_PASSWORD_LOAD,
            host=POSTGRES_HOST_LOAD,
            port=POSTGRES_PORT_LOAD
        )
cursor = connection.cursor()