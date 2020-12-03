install:
	pip3 install -r requirements.txt

start-rq:
	rq worker --with-scheduler

all:
	FLASK_APP=app.py flask run

