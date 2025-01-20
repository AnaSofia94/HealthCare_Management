# Healthcare Management API

This project provides a RESTful API for managing healthcare patient information while adhering to FHIR standards.

## Features
- Add, retrieve, update, and delete patient records.
- FHIR-compliant data model.
- Basic token-based authentication.
- API documentation using Swagger.

## Requirements
- Python 3.11+
- Django 4.0+
- PostgreSQL

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/HealthCare_Management.git
   cd HealthCare_Management
   ```

2. Install dependencies:
   ```bash
   pipenv install
   pipenv shell
   ```

3. Set up the database:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

## Running the Application

Start the development server:
```bash
python manage.py runserver
```

## Authentication (Token)

The API uses token-based authentication. To generate a token for a user:

### Using Django Shell
```bash
python manage.py shell
```
Then:
```python
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

user = User.objects.get(username='your-username')
token, created = Token.objects.get_or_create(user=user)
print(f'Token for user {user.username}: {token.key}')
```

### Using Management Command
You can also generate a token using a custom management command:
```bash
python manage.py generate_token your-username
```

#### Response:
```json
{
    "token": "your-generated-token"
}
```

## Endpoints

### Patients
- **POST /fhir/Patient/**: Add a new patient record.
- **GET /fhir/Patient/**: Retrieve a list of all patients.
- **GET /fhir/Patient/{id}/**: Retrieve details of a specific patient by ID.
- **PUT /fhir/Patient/{id}/**: Update the details of a specific patient.
- **DELETE /fhir/Patient/{id}/**: Delete a specific patient record.

## API Documentation

Swagger is used for API documentation.

### Access Swagger UI
Run the server and navigate to:
```
http://127.0.0.1:8000/swagger/
```

### Swagger JSON
To fetch the JSON documentation:
```bash
curl http://127.0.0.1:8000/swagger.json
```

## Deployment

### Docker

1. Build the Docker image:
   ```bash
   docker build -t healthcare_api .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 healthcare_api
   ```

### Environment Variables
Ensure the following environment variables are set:
- `DJANGO_SECRET_KEY`
- `DATABASE_URL`

You can use a `.env` file to manage these variables.

### Notes
If the `fhir.resources` package is not installed via `pipenv`, you can install it manually:
```bash
pip install fhir.resources
```
Alternatively, add it directly to your `Pipfile` using:
```bash
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
fhir.resources = "*"
```

## Testing

Run tests using:
```bash
python manage.py test
```