FROM python:3.11.5-slim

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD /app /app
WORKDIR /app

CMD python manage.py runserver 0.0.0.0:8000
