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

worker:
	cd app && celery -A settings worker -l info

beat:
	cd app && celery -A settings beat -l info

show_urls:
	$(manage_py) show_urls

pytest:
	pytest app/tests/ --cov=app --cov-report html

show-coverage:  ## open coverage HTML report in default browser
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"

gunicorn:
	cd app && gunicorn -w 4 settings.wsgi:application -b 0.0.0.0:8001 --log-level=DEBUG


