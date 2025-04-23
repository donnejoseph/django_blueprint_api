# Django Blueprint API

A robust Django REST framework blueprint project for building scalable and maintainable APIs.

## Features

- Django 5.1.3 with Django REST Framework 3.15.2
- PostgreSQL database integration
- Docker containerization for development and deployment
- Database health check with custom management command
- Production-ready configuration with separate development settings
- Modern code formatting and linting tools
- Docker health checks for services
- Latest Python 3.12 and Postgres 16 images

## Prerequisites

- Docker and Docker Compose
- Git

## Getting Started

### Clone the repository

```bash
git clone <repository-url>
cd django_blueprint_api
```

### Run with Docker

Build and start the containers:

```bash
docker-compose up
```

The API will be available at http://localhost:8000

### Development

To run linting:

```bash
docker-compose run --rm app sh -c "flake8"
```

To run tests (when added):

```bash
docker-compose run --rm app sh -c "pytest"
```

To format code:

```bash
docker-compose run --rm app sh -c "black ."
docker-compose run --rm app sh -c "isort ."
```

## Project Structure

```
app/
├── api/                  # Main API application
│   ├── management/       # Custom management commands
│   │   └── commands/     
│   │       └── wait_for_db.py  # Database connection health check
│   ├── tests/            # API tests
│   ├── models.py         # Database models
│   └── views.py          # API views with health check endpoint
└── config/               # Django project configuration
    ├── settings.py       # Project settings
    └── urls.py           # URL routing
```

## Configuration

Environment variables for database connection:

- `DB_HOST`: PostgreSQL host
- `DB_NAME`: Database name
- `DB_USER`: Database user
- `DB_PASS`: Database password
- `DEBUG`: Debug mode (1=on, 0=off)
- `SECRET_KEY`: Django secret key

## Docker Setup

The project uses:
- Python 3.12 with Alpine 3.19 for the application container
- PostgreSQL 16 with Alpine for the database
- Health checks for both services
- Volume mounts for persistent data
- Multi-stage build for efficient images

## Dependencies

### Main Dependencies

- Django 5.1.3
- Django REST Framework 3.15.2
- psycopg2 2.9.9

### Development Dependencies

- flake8 6.2.0
- pytest 8.1.0
- pytest-django 5.1.0
- black 24.5.0
- isort 5.13.0

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]