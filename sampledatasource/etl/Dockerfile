FROM python:3.6-slim

COPY ./etl/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./etl/etl.py .

# ENTRYPOINT ["/bin/echo", "Hello you."]

CMD ["python", "etl.py"]
