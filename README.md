# POSTGRES DUMPER & UPLOADER (Restore)

- [Postgres Dumper & Uploader](#postgres-dumper--uploader)
- [Description](#description)
- [Installing](#installing)
- [Run Dump](#run-dump)
- [Run Upload](#run-upload)
- [Author](#author)
- [Version](#version)

___
# Description
* <b> Dump data from the selected PostgreSQL database </b>
* <b> SQL file data uploading into selected PostgreSQL database </b>

<span style="color:red">Note:</span><br/>
The dump and upload functions operate independently; it is sufficient to specify the database information for the function you are using.<br/>
<span style="color:red">Note 2:</span><br/>
Whichever database you want to load into or pull data from, your device's IP address must have access permission to that database.<br/>
<span style="color:red">Note 3:</span><br/>
If a table or column name conflicts with certain global SQL keywords (e.g., "<span style="color:#007FFF">order</span>", "<span style="color:#007FFF">default</span>"), precautions have been taken to handle it. Additionally, measures have been implemented to handle specific characters within string column values.
____

# Installing

Create a virtual environment
Example:           

``` 
$ python3 -m venv env     #macos/linux

> py -3 -m venv env       #windows
```

Activate the virtual environment.

```
$ source env/bin/activate #macos/linux

> env\Scripts\activate    #windows
```
Install the dependencies listed in the requirements.txt file into the virtual environment.

```
$ pip install -r requirements.txt
```

Create a .env file in the main directory and add the following content to it:
<b style="color:#007FFF">SQL_OUTPUT</b> - The path where the SQL file will be created.
<b style="color:#007FFF">SQL_INPUT</b> - The path where the SQL file is selected.

```
###################################################################
###                       POSTGRES DUMP                         ###
###   The database from which you are trying to retrieve data   ###
###################################################################

POSTGRES_DB_DUMP=dump_database
POSTGRES_USER_DUMP=dump_username
POSTGRES_PASSWORD_DUMP=dump_password
POSTGRES_HOST_DUMP=dump_host
POSTGRES_PORT_DUMP=dump_port

SQL_OUTPUT=backup_postgresql.sql

###################################################################
###                       POSTGRES UPLOAD                       ###
###       The database where you want to upload the data        ###
###################################################################

POSTGRES_DB_UPLOAD=upload_to_database
POSTGRES_USER_UPLOAD=upload_to_user
POSTGRES_PASSWORD_UPLOAD=upload_to_password
POSTGRES_HOST_UPLOAD=upload_to_host
POSTGRES_PORT_UPLOAD=upload_to_port

SQL_INPUT=backup_postgresql.sql
```
___

# Run Dump


If you have placed the <span style="color:#007FFF">POSTGRES DUMP</span> information inside the <span style="color:#007FFF">.env</span> file, navigate to the <span style="color:#007FFF">dump</span> folder and run the <span style="color:#007FFF">dumper.py</span> file. An SQL file will be created with the name you assigned to the <span style="color:#007FFF">SQL_OUTPUT</span> variable in the <span style="color:#007FFF">.env</span> file.
If you want any column to auto-increment like an <span style="color:#007FFF">id</span>, you can add the column name to the <span style="color:#007FFF">autoincrement_list = ["id"]</span> inside <span style="color:#007FFF">dump/config.py</span>. For any table that contains this column, it will be treated as an auto-incrementing ID and saved accordingly.

___

# Run Upload

If you have placed the <span style="color:#007FFF">POSTGRES UPLOAD</span> information into the <span style="color:#007FFF">.env</span> file, navigate to the <span style="color:#007FFF">upload</span> folder and run the <span style="color:#007FFF">upload.py</span> file. The file specified in the <span style="color:#007FFF">SQL_INPUT</span> variable in the <span style="color:#007FFF">.env</span> will be uploaded into the selected database."

___

# Author

<b>Contributors names and contact info</b>

<b>ex. Pashayev Rafig - [PashaeFF - Github](https://github.com/PashaeFF) </b>

___
# Version

>* <b>v1.0</b>