FROM python:3.10

WORKDIR /webserver

COPY requirements.txt /webserver/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /webserver/requirements.txt

COPY .  /webserver
  

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]