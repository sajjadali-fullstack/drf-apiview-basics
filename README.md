# Django REST Framework - APIView Basics

A simple Django REST Framework project demonstrating how to build APIs using `APIView`.

## Features

- Class-Based APIView
- GET Request Handling
- JSON Responses
- Django REST Framework Integration

## Tech Stack

- Python
- Django
- Django REST Framework

## Project Structure

```
project/
│── testapp/
│── manage.py
```

## API Endpoint

### GET /

Response

```json
{
    "msg": "Happy Coding",
    "coding": [
        "python",
        "java",
        "javaScript",
        "c",
        "C++"
    ]
}
```

## Installation

```bash
git clone <repository-url>

cd drf-apiview-basics

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

## Author

Sajjad Ali
