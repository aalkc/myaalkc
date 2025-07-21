# Amanat Al-Kalima Company ERP System

## Overview

This is a comprehensive ERP (Enterprise Resource Planning) system designed specifically for Amanat Al-Kalima Company's metal scrap business operations in Saudi Arabia.

## System Architecture

### Backend (Python/FastAPI)
- **Framework**: FastAPI with Python 3.11+
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT-based authentication
- **Cache**: Redis for session management and caching
- **API Documentation**: Auto-generated OpenAPI/Swagger documentation

### Frontend (React/TypeScript)
- **Framework**: React 18 with TypeScript
- **Build Tool**: Vite for fast development and building
- **Styling**: Tailwind CSS for responsive design
- **State Management**: Zustand for global state
- **Data Fetching**: TanStack Query (React Query) for server state
- **Routing**: React Router for client-side routing

## Features

### Core Modules

1. **Inventory Management**
   - Track metal scrap inventory by category
   - Manage stock levels and locations
   - Monitor low stock alerts
   - Calculate inventory values

2. **Sales Management**
   - Create and manage customer orders
   - Track order status from pending to delivered
   - Generate invoices and receipts
   - Customer relationship management

3. **Purchasing Management**
   - Manage supplier relationships
   - Create and track purchase orders
   - Monitor delivery schedules
   - Supplier performance analysis

4. **Reports & Analytics**
   - Dashboard with key metrics
   - Inventory summaries by category
   - Sales performance reports
   - Financial reports and analytics

### Business Features

- **Multi-currency Support**: Primary currency SAR (Saudi Riyal)
- **Tax Calculation**: Automated VAT calculation (15% Saudi VAT)
- **Arabic Support**: Bilingual interface (Arabic/English)
- **Role-based Access**: Admin and user roles
- **Real-time Updates**: Live data synchronization

## API Documentation

The backend provides a comprehensive REST API with automatic OpenAPI documentation available at `/docs` when running the development server.

### Authentication
All API endpoints (except login) require JWT token authentication passed as `Authorization: Bearer <token>` header.

### Endpoints Overview

- `POST /api/v1/auth/access-token` - Login
- `GET /api/v1/inventory/` - List inventory items
- `POST /api/v1/inventory/` - Create inventory item
- `GET /api/v1/sales/` - List sale orders
- `POST /api/v1/sales/` - Create sale order
- `GET /api/v1/purchasing/` - List purchase orders
- `GET /api/v1/reports/dashboard` - Dashboard statistics

## Development Setup

### Prerequisites
- Docker and Docker Compose
- Node.js 18+ (for frontend development)
- Python 3.11+ (for backend development)

### Quick Start with Docker
```bash
git clone <repository-url>
cd myaalkc
docker-compose up -d
```

Access points:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### Local Development

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Deployment

The system is containerized and can be deployed using Docker Compose or individual containers.

### Environment Variables

#### Backend
- `DATABASE_URL`: PostgreSQL connection string
- `REDIS_URL`: Redis connection string
- `SECRET_KEY`: JWT secret key
- `FIRST_SUPERUSER`: Initial admin email
- `FIRST_SUPERUSER_PASSWORD`: Initial admin password

#### Frontend
- `VITE_API_URL`: Backend API URL

## Security

- JWT-based authentication with configurable expiration
- Password hashing using bcrypt
- CORS configuration for secure cross-origin requests
- Input validation using Pydantic
- SQL injection prevention through ORM
- XSS protection headers

## License

Private - Amanat Al-Kalima Company