from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

POSTGRES_DB_UPLOAD = os.getenv("POSTGRES_DB_UPLOAD")
POSTGRES_USER_UPLOAD = os.getenv("POSTGRES_USER_UPLOAD")
POSTGRES_PASSWORD_UPLOAD = os.getenv("POSTGRES_PASSWORD_UPLOAD")
POSTGRES_HOST_UPLOAD = os.getenv("POSTGRES_HOST_UPLOAD")
POSTGRES_PORT_UPLOAD = os.getenv("POSTGRES_PORT_UPLOAD")


input_file = os.getenv("SQL_INPUT")

connection = psycopg2.connect(
            database=POSTGRES_DB_UPLOAD,
            user=POSTGRES_USER_UPLOAD,
            password=POSTGRES_PASSWORD_UPLOAD,
            host=POSTGRES_HOST_UPLOAD,
            port=POSTGRES_PORT_UPLOAD
        )
cursor = connection.cursor()