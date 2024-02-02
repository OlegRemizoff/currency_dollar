run:
	python manage.py runserver

shell:
	python manage.py shell

makemigrations:
	python manage.py makemigrations

migrate: makemigrations
	python manage.py migrate

su:
	python manage.py createsuperuser

celery:
	celery -A config worker -l info