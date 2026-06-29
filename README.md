# DRF — APIView & ViewSet Demo

A simple Django REST Framework project demonstrating APIs using `APIView` 
and `ViewSet` with `DefaultRouter`.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-red?style=flat&logo=django&logoColor=white)

---

## API Endpoints

### APIView — `/api/`

| Method | Response |
|---|---|
| GET | Returns list of coding languages |
| POST | Accepts `name`, returns personalized message |
| PUT | Confirms PUT method |
| PATCH | Confirms PATCH method |
| DELETE | Confirms DELETE method |

### ViewSet — `/test-view-set/`

| Action | Method | Response |
|---|---|---|
| list | GET | Returns list of colours |
| retrieve | GET `/pk/` | Fetch single item |
| partial_update | PATCH `/pk/` | Partial update |
| destroy | DELETE `/pk/` | Delete item |

---

## Screenshots

### Browsable API — GET `/api/`
![DRF GET](screenshots/restapi-withrest2.png)

### POST `/api/` — DRF Browsable
![DRF POST](screenshots/restapi-post-withoutrest2.png)

### Postman — GET `/api/`
![Postman GET](screenshots/postman-test-api-withrest2.png)

### Postman — POST `/api/`
![Postman POST](screenshots/postman-postreq-withrest2.png)

### Postman — PUT `/api/`
![Postman PUT](screenshots/postman-put.png)

### Postman — PATCH `/api/`
![Postman PATCH](screenshots/postman-patch.png)

### Postman — DELETE `/api/`
![Postman DELETE](screenshots/postman-delete.png)

### Postman — GET `/` (Router)
![Postman Router](screenshots/postman-api-route1.png)

### Postman — GET `/test-view-set/`
![Postman ViewSet](screenshots/postman-api-route2.png)

---

## Sample Responses

**GET /api/**
```json
{
    "msg": "Happy Coding",
    "coding": ["python", "java", "C#", "javaScript", "C++"]
}
```

**POST /api/**
```json
{
    "msg": "Hey Sajjad Ali, Happy ending of DRF classes"
}
```

**GET /test-view-set/**
```json
{
    "msg": "Learning DRF",
    "colours": ["red", "green", "blue"]
}
```

---

## Setup

```bash
git clone https://github.com/sajjadali-fullstack/drf-apiview-viewset-demo.git
cd drf-apiview-viewset-demo
pip install -r requirements.txt
python manage.py runserver
```

---

## Author

**Sajjad Ali** — [GitHub](https://github.com/sajjadali-fullstack) · 
[Portfolio](https://sajjadali-fullstack-portfolio.netlify.app/)
