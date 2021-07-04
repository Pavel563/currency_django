SHELL := /bin/bash

manage_py := python ./app/manage.py

runserver:
	$(manage_py) runserver

migrate:
	$(manage_py) migrate

generate_data:
	$(manage_py) generate_data
