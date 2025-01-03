# Deployment Guide for Healthcare API

This document outlines the steps to deploy the Healthcare API on a cloud platform.

---

## Prerequisites

Before deployment, ensure you have the following installed:
- **Python** (Version 3.11 or later)
- **Pip** (Package Installer for Python)
- **Docker** (For containerization, optional)
- **Heroku CLI**, **AWS CLI**, or **gcloud** (depending on the cloud platform)
- A **PostgreSQL** database set up (local or cloud)

---

## Deployment Steps

### 1. Set Up the Production Environment

1. **Install Production Dependencies**:
   ```bash
   pip install gunicorn whitenoise psycopg2-binary
   ```

2. **Update `settings.py`**:
   - Set `DEBUG = False`:
     ```python
     DEBUG = False
     ```
   - Configure `ALLOWED_HOSTS`:
     ```python
     ALLOWED_HOSTS = ['your-domain.com', 'your-cloud-ip']
     ```
   - Configure `STATIC_URL` and `STATIC_ROOT`:
     ```python
     STATIC_URL = '/static/'
     STATIC_ROOT = BASE_DIR / 'staticfiles'
     ```
   - Use an environment variable for the `SECRET_KEY`:
     ```python
     import os
     SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default-insecure-key')
     ```

3. **Create a `.env` File** (Optional):
   Store environment variables in a `.env` file:
   ```plaintext
   DJANGO_SECRET_KEY=your-secret-key
   DJANGO_DEBUG=False
   ```

4. **Collect Static Files**:
   ```bash
   python manage.py collectstatic --noinput
   ```

---

### 2. Dockerize the Application (Optional)

1. **Create a `Dockerfile`**:
   ```dockerfile
   FROM python:3.11
   ENV PYTHONDONTWRITEBYTECODE 1
   ENV PYTHONUNBUFFERED 1
   WORKDIR /app
   COPY . /app
   RUN pip install --upgrade pip
   RUN pip install -r requirements.txt
   RUN python manage.py collectstatic --noinput
   EXPOSE 8000
   CMD ["gunicorn", "healthcare_api.wsgi:application", "--bind", "0.0.0.0:8000"]
   ```

2. **Create a `docker-compose.yml`**:
   ```yaml
   version: "3.9"

   services:
     web:
       build: .
       ports:
         - "8000:8000"
       env_file:
         - .env
       depends_on:
         - db

     db:
       image: postgres:14
       environment:
         POSTGRES_DB: healthcare
         POSTGRES_USER: admin
         POSTGRES_PASSWORD: adminpassword
   ```

3. **Build and Run**:
   ```bash
   docker-compose up --build
   ```

---

### 3. Deploy to Heroku (Example)

1. **Install Heroku CLI**:
   ```bash
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. **Create a `Procfile`**:
   ```plaintext
   web: gunicorn healthcare_api.wsgi --log-file -
   ```

3. **Login to Heroku**:
   ```bash
   heroku login
   ```

4. **Create a New Heroku App**:
   ```bash
   heroku create your-app-name
   ```

5. **Add PostgreSQL**:
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

6. **Set Environment Variables**:
   ```bash
   heroku config:set DJANGO_SECRET_KEY='your-secret-key'
   ```

7. **Deploy the App**:
   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git push heroku main
   ```

---

### 4. Deploy to AWS (Example)

1. **Install AWS CLI**:
   ```bash
   pip install awscli
   ```

2. **Initialize Elastic Beanstalk**:
   ```bash
   eb init
   ```

3. **Create an Environment**:
   ```bash
   eb create django-env
   ```

4. **Deploy the App**:
   ```bash
   eb deploy
   ```

---

### 5. Deploy to GCP (Example)

1. **Install gcloud CLI**:
   ```bash
   curl https://sdk.cloud.google.com | bash
   ```

2. **Initialize the Project**:
   ```bash
   gcloud init
   ```

3. **Create an `app.yaml` File**:
   ```yaml
   runtime: python311
   entrypoint: gunicorn -b :$PORT healthcare_api.wsgi
   ```

4. **Deploy the App**:
   ```bash
   gcloud app deploy
   ```

---

## Post-Deployment Checklist

1. Test the application:
   ```bash
   curl http://your-domain.com
   ```
2. Set up logging and monitoring on the cloud platform.
3. Scale the application as needed.

---

## Notes

- Ensure sensitive information (e.g., `SECRET_KEY`, database credentials) is managed securely using environment variables.
- Use a reverse proxy like Nginx for additional security and performance optimization in production.
