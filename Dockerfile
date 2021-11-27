# Use the LTS release.
FROM python:3.9.4-slim-buster

# RUN useradd --user-group --create-home --shell /bin/false app 

WORKDIR /home/Altair/docker-sample

ADD . .

#ADD app.py .

RUN pip install -r requirements.txt

CMD ["python3":"app.py"]

# USER app