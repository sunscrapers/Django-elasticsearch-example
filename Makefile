.PHONY: build up down attach bootstrap bash shell migrate migrations
build:
	docker compose build

up:
	make build
	docker compose up

down:
	docker compose down

attach:
	docker attach django_app

bootstrap:
	docker exec -it django_app python manage.py bootstrap

bash:
	docker exec -it django_app bash

shell:
	docker exec -it django_app python manage.py shell

migrate:
	docker exec -it django_app python manage.py migrate

migrations:
	docker exec -it django_app python manage.py makemigrations
