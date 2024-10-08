from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

POSTGRES_DB_DUMP = os.getenv("POSTGRES_DB_DUMP")
POSTGRES_USER_DUMP = os.getenv("POSTGRES_USER_DUMP")
POSTGRES_PASSWORD_DUMP = os.getenv("POSTGRES_PASSWORD_DUMP")
POSTGRES_HOST_DUMP = os.getenv("POSTGRES_HOST_DUMP")
POSTGRES_PORT_DUMP = os.getenv("POSTGRES_PORT_DUMP")

output_file = "backup_postgresql.sql"

autoincrement_list = ["id"]


connection = psycopg2.connect(
            database=POSTGRES_DB_DUMP,
            user=POSTGRES_USER_DUMP,
            password=POSTGRES_PASSWORD_DUMP,
            host=POSTGRES_HOST_DUMP,
            port=POSTGRES_PORT_DUMP
        )
cursor = connection.cursor()