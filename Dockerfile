FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir flask python-dotenv mysql-connector-python numpy

COPY . /app

EXPOSE 5001

CMD ["python", "app.py"]