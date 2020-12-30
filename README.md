## Contents

1. [Initial Setup Instructions](#initial-setup-instructions)
2. [Running Server](#running-server)


## Initial Setup Instructions

### Setup Python Virtual Environment
```buildoutcfg
python -m venv venv                 // create virtual environment
source venv/Script/activate         // activate the virtual env
                                    // to deactivate the virtual environment just run: 'deactivate'
pip freeze                          // check if requirements are installed
pip freeze > requirements.txt       // write list of requirements in requirements.txt file
pip install -r requirements.txt     // install requirements
```
## Running Server
### Cheatsheet
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
python app.py               // launch server
```
### Go and check `http://127.0.0.1:5000`

## Managin the database
use request, redirect, url_for from Falsk
"from flask import Flask, render_template, request, redirect, url_for"
```buildoutcfg
### Go into the python console then:

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
