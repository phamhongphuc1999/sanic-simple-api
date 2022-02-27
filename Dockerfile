FROM python:3.8

WORKDIR /sanic_app

COPY . /sanic_app
RUN pip3 install -r requirements/production.txt
CMD [ "python", "main.py" ]