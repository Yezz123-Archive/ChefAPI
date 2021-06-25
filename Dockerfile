FROM python:3.7

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY api /app/api
COPY core /app/core
COPY crud /app/crud
COPY database /app/database
COPY models /app/models
COPY schema /app/schema
COPY config.py /app/config.py
COPY main.py /app/main.py

RUN python3 -m pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]