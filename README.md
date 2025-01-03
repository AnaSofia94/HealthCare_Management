# HealthCare_Management

# Healthcare API

This is a RESTful API for managing patient information in a healthcare setting, built using Django and Django REST Framework (DRF). The API is designed to comply with the FHIR (Fast Healthcare Interoperability Resources) standard.

---


## Features

- **CRUD Operations**:
  - Create, Read, Update, and Delete patient information.
- **FHIR Compliance**:
  - Structured according to FHIR standards for patient resources.
- **Authentication**:
  - Token-based authentication for secure access.
- **Swagger API Documentation**:
  - Interactive API documentation using Swagger.
- **PostgreSQL Support**:
  - Persistent database storage.

---

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Deployment**: Gunicorn, WhiteNoise, Docker
- **API Documentation**: DRF-YASG (Swagger)
- **Python Version**: 3.11

---

## Installation and Setup

### Prerequisites

- Python 3.11+
- PostgreSQL
- Pipenv (for managing virtual environments)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/healthcare-api.git
cd healthcare-api
```

### Step 2: Set Up the Virtual Environment

1. Install `pipenv`:
   ```bash
   pip install pipenv
   ```

2. Install dependencies:
   ```bash
   pipenv install
   ```

3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

### Step 3: Configure the Database

1. Create a PostgreSQL database:
   ```sql
   CREATE DATABASE healthcare_api;
   ```

2. Update the `DATABASES` configuration in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'healthcare_api',
           'USER': 'your_user',
           'PASSWORD': 'your_password',
           'HOST': '127.0.0.1',
           'PORT': '5432',
       }
   }
   ```

### Step 4: Apply Migrations

```bash
python manage.py migrate
```

### Step 5: Run the Development Server

```bash
python manage.py runserver
```

---

## API Endpoints

### Patient Resource

| Method | Endpoint                     | Description                     |
|--------|-------------------------------|---------------------------------|
| POST   | `/fhir/Patient/`             | Add a new patient record.      |
| GET    | `/fhir/Patient/`             | Retrieve a list of all patients. |
| GET    | `/fhir/Patient/{id}/`        | Retrieve a specific patient.   |
| PUT    | `/fhir/Patient/{id}/`        | Update a specific patient.     |
| DELETE | `/fhir/Patient/{id}/`        | Delete a specific patient.     |

---

## Authentication

This API uses token-based authentication. Obtain a token by sending your credentials to the `/api/token/` endpoint.

- **Header Example**:
  ```http
  Authorization: Token <your-token>
  ```

---

## Deployment

### Docker Deployment

1. Build the Docker image:
   ```bash
   docker build -t healthcare-api .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 healthcare-api
   ```

---

## API Documentation

Access the Swagger UI for interactive API documentation at:
```
http://127.0.0.1:8000/swagger/
```

---

## Testing

Run tests to ensure the API is working as expected:
```bash
python manage.py test
```

---

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature-name"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
