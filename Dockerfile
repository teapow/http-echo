FROM python:3-alpine

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./src /app

CMD ["python", "/app/app.py"]