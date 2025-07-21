# myaalkc

Customer Management API built with FastAPI and SQLAlchemy.

## Features

- **Customer CRUD Operations**: Create, read, and list customers
- **FastAPI Integration**: Modern, fast web framework with automatic API documentation
- **SQLAlchemy ORM**: Database operations with MySQL support
- **Data Validation**: Request/response validation using Pydantic schemas
- **Error Handling**: Proper HTTP status codes and error messages

## API Endpoints

### Customer Management

- `POST /customers/` - Create a new customer
- `GET /customers/` - Get all customers (with pagination)
- `GET /customers/{customer_id}` - Get a customer by ID

### Documentation

- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables (see `.env.example`):
```bash
cp .env.example .env
# Edit .env with your database configuration
```

## Usage

### Start the API Server

```bash
uvicorn backend.main:app --reload
```

The API will be available at `http://localhost:8000`

### Example API Calls

#### Create a Customer
```bash
curl -X POST "http://localhost:8000/customers/" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "John Doe",
       "email": "john.doe@example.com",
       "phone": "+1-555-0123",
       "address": "123 Main St, Anytown, USA"
     }'
```

#### Get All Customers
```bash
curl -X GET "http://localhost:8000/customers/"
```

#### Get Customer by ID
```bash
curl -X GET "http://localhost:8000/customers/1"
```

### Run Example Script

```bash
python example_usage.py
```

## Project Structure

```
backend/
├── __init__.py
├── main.py              # FastAPI application
├── database.py          # Database connection and session management
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic request/response schemas
├── customer_crud.py     # Customer CRUD operations
└── routers/
    ├── __init__.py
    └── customer_router.py # Customer API endpoints
```

## Database Schema

### Customer Table

| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key (auto-increment) |
| name | String(255) | Customer name |
| email | String(255) | Customer email (unique) |
| phone | String(50) | Customer phone (optional) |
| address | Text | Customer address (optional) |
| created_at | DateTime | Record creation timestamp |
| updated_at | DateTime | Record update timestamp |

## Dependencies

- FastAPI >= 0.104.0
- SQLAlchemy >= 1.4.0
- Pydantic >= 2.0.0
- mysql-connector-python >= 8.0.0
- uvicorn >= 0.24.0
- httpx >= 0.24.0