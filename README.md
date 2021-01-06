## Contents

1. [Initial Setup Instructions](#initial-setup-instructions)
2. [Running Server](#running-server)

## Quick start the app
Use the following commands to launch and try the app
* Notice that you must install python before
```buildoutcfg 
python -m venv venv
source venv/Script/activate
pip install -r requirements.txt

./manage.py makemigrations
./manage.py migrate
./manage.py createuseruser

./manage.py runserver
```

## Initial Setup Instructions

### Setup Python Virtual Environment
```buildoutcfg
python -m venv venv                 // create virtual environment
source venv/Script/activate         // activate the virtual env
                                    // to deactivate the virtual environment just run: 'deactivate'
pip install -r requirements.txt     // install requirements
pip freeze                          // check if requirements were well installed
```
## Running Server
```buildoutcfg
./manage.py runserver       // launch server
```
### Go and check `http://127.0.0.1:8000`


## Create a module
```buildoutcfg 
./manage.py startapp <module>
```
Go to settings.py inside app folder (ie. django_movie_app) and add the new module (ie. movies)
```buildoutcfg 
INSTALLED_APPS = [
    ...
    'movies',
]
```

## Create model (database) for a module
Go to <module>/models.py and create one class for each table using 'models.Model' as parameter for the class constructor
'documentation: https://docs.djangoproject.com/en/3.1/ref/models/fields/'

```buildoutcfg ```
## Manage the database
Create database from information given in movies/models.py
Django convert python code to SQL code and create database and table(s)
```buildoutcfg 
./manage.py makemigrations                  // create our tables
./manage.py migrate                         // add our tables and django tables to database
./manage.py createsuperuser                 // create user admin
```

### From the python console
```buildoutcfg
sqlite3 todo.db             // create database
    .tables                 // no tables have been created yet
    .exit
python
    from app import db
    db.create_all()         // create tables for the database
    exit()
sqlite3 todo.db             // access to the database
    .tables                 // show the tables
    .exit
```

### Go into the python console then:
use request, redirect, url_for from Falsk
"from flask import Flask, render_template, request, redirect, url_for"
```buildoutcfg

from app import db              // call the database to use
db                              // check database
from app import Todo            // call table to be used
Todo.query.all()                // check content, return ==> []
todo_1 = Todo(text='do laundry', complete=False)           // create entry/item/element
todo_1                          // check element
todo_1.text                     // check element content
Todo.query.all()                // check content ==> empty for the moment ==> []
db.session.add(todo_1)          // add entry
Todo.query.all()                // check table content
db.session.commit()             // save the database changes
Todo.query.filter_by(complete=False).all()              // filtering results
```
