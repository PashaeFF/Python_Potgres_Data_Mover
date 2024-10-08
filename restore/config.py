from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

POSTGRES_DB_RESTORE = os.getenv("POSTGRES_DB_RESTORE")
POSTGRES_USER_RESTORE = os.getenv("POSTGRES_USER_RESTORE")
POSTGRES_PASSWORD_RESTORE = os.getenv("POSTGRES_PASSWORD_RESTORE")
POSTGRES_HOST_RESTORE = os.getenv("POSTGRES_HOST_RESTORE")
POSTGRES_PORT_RESTORE = os.getenv("POSTGRES_PORT_RESTORE")
OUTPUT_FILE = "backup_postgresql.sql"


connection = psycopg2.connect(
            database=POSTGRES_DB_RESTORE,
            user=POSTGRES_USER_RESTORE,
            password=POSTGRES_PASSWORD_RESTORE,
            host=POSTGRES_HOST_RESTORE,
            port=POSTGRES_PORT_RESTORE
        )
cursor = connection.cursor()