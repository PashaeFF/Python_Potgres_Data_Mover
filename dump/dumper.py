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
                
                # CREATE TABLE for table
                cursor.execute(f"""
                    SELECT 'CREATE TABLE ' || table_name || ' (' || string_agg(column_name || ' ' || data_type, ', ') || ');'
                    FROM information_schema.columns
                    WHERE table_name='{table_name}'
                    GROUP BY table_name;
                """)
                create_table_query = cursor.fetchone()[0]
                f.write(create_table_query + "\n")

                # INSERT table datas
                cursor.execute(f"SELECT * FROM {'\"order\"' if table_name == "order" else table_name};")
                rows = cursor.fetchall()
                for row in rows:
                    values = ', '.join([f"'{str(value)}'" if value is not None else 'NULL' for value in row])
                    insert_query = f"INSERT INTO {table_name} VALUES ({values});"
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

