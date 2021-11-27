FROM python:3.9.4-slim-buster

ADD ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

ADD . .

CMD ["python3","app.py"]