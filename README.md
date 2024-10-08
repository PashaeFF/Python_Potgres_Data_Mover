# POSTGRES DUMPER & LOADER

- [Postgres Dumper & Loader](#postgres-dumper--loader)
- [Project Title](#project-title)
- [Description](#description)
- [Installing](#installing)
- [Run Dump](#run-dump)
- [Run Load](#run-load)
- [Author](#author)

___

# Project Title
___
* <b>Postgres Dumper & Loader</b>
___

# Description
___
* <b> Dump data from the selected PostgreSQL database </b>
* <b> SQL file data loading into selected PostgreSQL database </b>

<b> Note: The dump and load functions operate independently; it is sufficient to specify the database information for the function you are using. </b>
____

# Installing

Create a virtual environment
Example:           

``` 
$ python3 -m venv env
```

Activate the virtual environment.

```
$ source env/bin/activate
```
Install the dependencies listed in the requirements.txt file into the virtual environment.

```
$ pip install -r requirments.txt
```

Create a .env file in the main directory and add the following content to it:
<b>SQL_OUTPUT</b> - The path where the SQL file will be created.
<b>SQL_INPUT</b> - The path where the SQL file is selected.

```
###############################################################
###                     POSTGRES DUMP                       ###
### The database from which you are trying to retrieve data ###
###############################################################

POSTGRES_DB_DUMP=dump_database
POSTGRES_USER_DUMP=dump_username
POSTGRES_PASSWORD_DUMP=dump_password
POSTGRES_HOST_DUMP=dump_host
POSTGRES_PORT_DUMP=dump_port

SQL_OUTPUT=backup_postgresql.sql  # sql output path

######################################################
###                 POSTGRES LOAD                  ###
### The database where you want to upload the data ###
######################################################

POSTGRES_DB_LOAD=loaded
POSTGRES_USER_LOAD=postgres
POSTGRES_PASSWORD_LOAD=postgres
POSTGRES_HOST_LOAD=localhost
POSTGRES_PORT_LOAD=5432

SQL_INPUT=backup_postgresql.sql # 
```

___

# Run Dump


If you have placed the <b>POSTGRES DUMP</b> information inside the <b>.env</b> file, navigate to the <b>dump</b> folder and run the <b>dumper.py</b> file. An SQL file will be created with the name you assigned to the <b>SQL_OUTPUT</b> variable in the <b>.env</b> file.

___

# Run Load

If you have placed the <b>POSTGRES LOAD</b> information into the <b>.env</b> file, navigate to the <b>load_sql_file_to_db</b> folder and run the <b>load.py</b> file. The file specified in the <b>SQL_INPUT</b> variable in the <b>.env</b> will be loaded into the selected database."

___

# Author

<b>Contributors names and contact info</b>

<b>ex. Pashayev Rafig - [PashaeFF - Github](https://github.com/PashaeFF) </b>

# Version

>* <b>v1.0</b>
___