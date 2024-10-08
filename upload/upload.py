from config import *

def upload_sql_file_to_db(sql_file):
    try:
        # Open and read the sql file
        with open(sql_file, 'r') as file:
            sql_commands = file.read()

        cursor.execute(sql_commands)

        # Update changes
        connection.commit()
        print(f"Data from the '{sql_file}' file has been successfully uploaded.")

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


upload_sql_file_to_db(sql_file=input_file)
