Gettyhub
========

A simple landpage that shows all you'r starred repos!


### Instalation

First you will need to create a PostgresSQL database for this project, to do this just execute the *base.sql* file as follows:
```bash
psql -f base.sql
```
This SQL file will create the test and production databases.

After this you only need to install the python related libraries and execute the django setup commands, first we install the requirements.


```bash
virtualenv .env
source .env/bin/active
pip install -r requirements.txt
```

then

```bash
./manage.py migrate
```
it should ouput something like this:
```text
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, repository, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying repository.0001_initial... OK
  Applying repository.0002_auto_20171010_0008... OK
  Applying sessions.0001_initial... OK
```



### Importing starred repos

For this task there is a simple django command, just execute the line below:

```bash
./manage.py import_repos
Github username: jdsolucoes
Importing....
```


### Testing
To run the tests just execute the test django command;
```bash
./manage.py test
```

### Running
To run this project just execute
```bash
./manage.py runserver

Performing system checks...

System check identified no issues (0 silenced).
October 10, 2017 - 14:23:20
Django version 1.11.6, using settings 'gettyhub.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Just visit http://127.0.0.1:8000/ and voila!