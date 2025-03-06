# Telegram Auth

## Overview
Telegram Auth is a Django-based application that provides a REST API for user authentication via Telegram. It includes robust test coverage using `pytest` and `pytest-django`.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.10+
- Virtual environment (`venv`)
- PostgreSQL or SQLite (default)

### Setup
Clone the repository:
```bash
git clone https://github.com/your-repo/poll_app.git
cd poll_app
```

Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run migrations:
```bash
python manage.py migrate
```

Create a superuser:
```bash
python manage.py createsuperuser
```

Run the development server:
```bash
python manage.py runserver
```

## API Endpoints
### Telegram Authentication
- **Register User**: `POST /api/auth/tg`
- **Get All Users**: `GET /api/auth/users`
- **Get Specific User**: `GET /api/auth/users/<telegram_id>`

## Running Tests
### Setup Pytest
Ensure `pytest` and `pytest-django` are installed:
```bash
pip install pytest pytest-django pytest-cov
```

### Configure `pytest.ini`
Create or modify `pytest.ini` in the project root:
```ini
[pytest]
DJANGO_SETTINGS_MODULE = root.settings
python_files = test_*.py tests.py
testpaths = apps/
addopts = --reuse-db -v --cov=apps --cov-report=term-missing
```

### Run Tests
To run all tests:
```bash
pytest
```
To check test coverage:
```bash
pytest --cov=apps --cov-report=term-missing
```
To generate an HTML coverage report:
```bash
pytest --cov=apps --cov-report=html
```
View the HTML report:
```bash
open htmlcov/index.html  # macOS/Linux
start htmlcov/index.html  # Windows
```

## Contribution
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to your branch (`git push origin feature-branch`)
5. Open a pull request

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---
Developed by **Your Name** 🚀

