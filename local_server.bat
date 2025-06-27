@echo off
set FLASK_APP=data_lakehouse/api/app.py
set FLASK_RUN_PORT=8000
set FLASK_RUN_HOST=0.0.0.0
flask run