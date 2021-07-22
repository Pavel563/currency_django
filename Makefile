SHELL := /bin/bash

manage_py := python3 ./app/manage.py

runserver:
	$(manage_py) runserver

migrations:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate

gd:
	$(manage_py) generate_data

freeze:
	$ pip freeze > requirements.txt

shell:
	$(manage_py) shell_plus --print-sql

superuser:
	$(manage_py) createsuperuser
