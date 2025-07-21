# Amanat Al-Kalima Company - ERP System

A comprehensive ERP application for metal scrap business operations in Saudi Arabia.

## Project Structure

- **backend/**: Python FastAPI backend application
- **frontend/**: React TypeScript frontend application
- **docs/**: Documentation and API specifications

## Technology Stack

### Backend
- **Framework**: FastAPI (Python)
- **Database**: PostgreSQL
- **Cache**: Redis
- **Authentication**: JWT
- **API Documentation**: OpenAPI/Swagger

### Frontend
- **Framework**: React 18
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State Management**: React Query + Zustand
- **Build Tool**: Vite

## Features

- **Inventory Management**: Track metal scrap inventory, categories, and stock levels
- **Sales Management**: Handle customer orders, invoicing, and sales tracking
- **Purchasing**: Manage supplier relationships and purchase orders
- **Financial Reports**: Generate comprehensive business reports
- **User Authentication**: Role-based access control
- **Multi-language Support**: Arabic and English

## Development Setup

### Prerequisites
- Docker and Docker Compose
- Node.js 18+ (for frontend development)
- Python 3.11+ (for backend development)

### Quick Start with Docker
```bash
# Clone the repository
git clone <repository-url>
cd myaalkc

# Start all services
docker-compose up -d

# Access the applications
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Documentation: http://localhost:8000/docs
```

### Local Development

#### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

#### Frontend Setup
```bash
cd frontend
npm install
npm start
```

## API Documentation

Once the backend is running, visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive API documentation.

## Project Status

🚧 **Under Development** - Initial project structure setup

## License

Private - Amanat Al-Kalima Company