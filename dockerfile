FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System deps for mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Collect static (optional but recommended)
RUN python manage.py collectstatic --noinput || true

# 🚀 THIS IS THE KEY FIX
CMD python manage.py migrate && python manage.py create_admin && gunicorn hostel_management.wsgi:application --bind 0.0.0.0:8000
