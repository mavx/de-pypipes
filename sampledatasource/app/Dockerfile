FROM python:3.6-slim

RUN pip install --no-cache-dir psycopg2-binary

COPY ./app/app.py .

CMD ["python", "app.py"]
