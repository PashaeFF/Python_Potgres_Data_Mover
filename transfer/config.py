from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

POSTGRES_DB_TRANSFER = os.getenv("POSTGRES_DB_TRANSFER")
POSTGRES_USER_TRANSFER = os.getenv("POSTGRES_USER_TRANSFER")
POSTGRES_PASSWORD_TRANSFER = os.getenv("POSTGRES_PASSWORD_TRANSFER")
POSTGRES_HOST_TRANSFER = os.getenv("POSTGRES_HOST_TRANSFER")
POSTGRES_PORT_TRANSFER = os.getenv("POSTGRES_PORT_TRANSFER")
OUTPUT_FILE = "backup_postgresql.sql"


connection = psycopg2.connect(
            database=POSTGRES_DB_TRANSFER,
            user=POSTGRES_USER_TRANSFER,
            password=POSTGRES_PASSWORD_TRANSFER,
            host=POSTGRES_HOST_TRANSFER,
            port=POSTGRES_PORT_TRANSFER
        )
cursor = connection.cursor()