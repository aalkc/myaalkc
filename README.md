# myaalkc

## Amanat Al-Kalima Company ERP API

A FastAPI-based Enterprise Resource Planning (ERP) API for Amanat Al-Kalima Company.

## Running the FastAPI Application

### Prerequisites

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Starting the Server

To run the FastAPI application using uvicorn, use the following command:

```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Command breakdown:**
- `cd backend` - Navigate to the backend directory (required for proper imports)
- `uvicorn main:app` - Run the FastAPI app from main.py
- `--reload` - Enable auto-reload on code changes (development mode)
- `--host 0.0.0.0` - Make the server accessible from any IP address
- `--port 8000` - Run the server on port 8000

### API Documentation (Swagger UI)

Once the server is running, you can access the automatic API documentation at:

**Swagger UI URL:** `http://localhost:8000/docs`

This interactive documentation allows you to:
- View all available API endpoints
- Test endpoints directly in the browser
- See request/response schemas
- Understand the API structure

### Alternative Documentation

FastAPI also provides ReDoc documentation at:

**ReDoc URL:** `http://localhost:8000/redoc`

### API Endpoints

- **Root endpoint:** `http://localhost:8000/` - Welcome message
- **Customer endpoints:** `http://localhost:8000/customers/` - Customer-related operations
- **OpenAPI JSON:** `http://localhost:8000/openapi.json` - API specification in JSON format

## Development

The application includes:
- CORS middleware for cross-origin requests
- Customer router for customer-related endpoints
- Automatic API documentation generation
- Hot reload for development