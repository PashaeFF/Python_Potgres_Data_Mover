from config import *

def dump_postgresql_to_sql(output_file):
    try:
        # Get all table names
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
        tables = cursor.fetchall()

        with open(output_file, 'w') as f:
            for table in tables:
                table_name = table[0]
                print("table > ", table_name)
                table_name_for_sql = f'"{table_name}"' if table_name == "order" else table_name
                # CREATE TABLE
                cursor.execute(f"""
                    SELECT 'CREATE TABLE ' || '{table_name_for_sql}' || ' (' || 
                        string_agg(
                            CASE 
                                WHEN column_name = 'default' THEN '\"' || column_name || '\" ' || data_type
                                ELSE column_name || ' ' || data_type 
                            END, 
                        ', ' ORDER BY ordinal_position) || 
                        ');'
                    FROM information_schema.columns
                    WHERE table_name='{table_name}'
                    GROUP BY table_name;
                """)

                create_table_query = cursor.fetchone()[0]

                
                f.write(create_table_query + "\n")

                # INSERT table datas
                cursor.execute(f"SELECT * FROM {table_name_for_sql};")
                rows = cursor.fetchall()
                for row in rows:
                    values = ""
                    for value in row:
                        if value is not None:
                            if isinstance(value, dict):
                                value = str(value)
                                str_value = str(value.replace("'","\""))
                                values += f", '{str_value}'"
                            elif isinstance(value, bool):
                                values += f", '{'TRUE' if value else 'FALSE'}'"
                            elif isinstance(value, int):
                                values += f", {value}"
                            elif isinstance(value, float):
                                values += f", {value}"
                            else:
                                str_value = str(value)
                                values += f", \'{str_value}\'"
                        else:
                            values += ", NULL"
                    values = values.lstrip(", ")
                    insert_query = f"INSERT INTO \"{table_name}\" VALUES ({values});"
                    f.write(insert_query + "\n")
        
        print(f"Database dump has been written to {output_file}")
    except Exception as error:
        print(f"Error occurred: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()


dump_postgresql_to_sql(
    output_file=OUTPUT_FILE
)

