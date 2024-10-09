# POSTGRES DUMPER & UPLOADER (Restore)

- [Postgres Dumper & Uploader](#postgres-dumper--uploader)
- [Description](#description)
- [Installing](#installing)
- [Run Dump](#run-dump)
- [Run Upload](#run-upload)
- [Author](#author)

___
# Description
___
* <b> Dump data from the selected PostgreSQL database </b>
* <b> SQL file data uploading into selected PostgreSQL database </b>

<b> <span style="color:red">Note:</span> The dump and upload functions operate independently; it is sufficient to specify the database information for the function you are using. </b><br/>
<b> <span style="color:red">Note 2:</span> Whichever database you want to load into or pull data from, your device's IP address must have access permission to that database.</b>
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
<b style="color:#007FFF">SQL_OUTPUT</b> - The path where the SQL file will be created.
<b style="color:#007FFF">SQL_INPUT</b> - The path where the SQL file is selected.

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

SQL_OUTPUT=backup_postgresql.sql

######################################################
###                POSTGRES UPLOAD                 ###
### The database where you want to upload the data ###
######################################################

POSTGRES_DB_UPLOAD=loaded
POSTGRES_USER_UPLOAD=postgres
POSTGRES_PASSWORD_UPLOAD=postgres
POSTGRES_HOST_UPLOAD=localhost
POSTGRES_PORT_UPLOAD=5432

SQL_INPUT=backup_postgresql.sql
```
___

# Run Dump


If you have placed the <b style="color:#007FFF">POSTGRES DUMP</b> information inside the <b style="color:#007FFF">.env</b> file, navigate to the <b style="color:#007FFF">dump</b> folder and run the <b style="color:#007FFF">dumper.py</b> file. An SQL file will be created with the name you assigned to the <b style="color:#007FFF">SQL_OUTPUT</b> variable in the <b style="color:#007FFF">.env</b> file.

___

# Run Upload

If you have placed the <b style="color:#007FFF">POSTGRES UPLOAD</b> information into the <b style="color:#007FFF">.env</b> file, navigate to the <b style="color:#007FFF">upload</b> folder and run the <b style="color:#007FFF">upload.py</b> file. The file specified in the <b style="color:#007FFF">SQL_INPUT</b> variable in the <b style="color:#007FFF">.env</b> will be uploaded into the selected database."

___

# Author

<b>Contributors names and contact info</b>

<b>ex. Pashayev Rafig - [PashaeFF - Github](https://github.com/PashaeFF) </b>

# Version

>* <b>v1.0</b>