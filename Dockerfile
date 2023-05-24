FROM python:3.11-slim
COPY requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt
COPY . /opt/app
WORKDIR /opt/app

CMD [ "python", "discogs/manage.py", "runserver", "0:8000" ]
