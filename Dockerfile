FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=run.py

RUN mkdir -p /app/instance && chmod -R 777 /app/instance

CMD ["flask", "run"]