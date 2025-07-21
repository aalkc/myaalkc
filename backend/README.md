# Backend

This directory contains the backend components for the myaalkc application.

## Database Connection

The `database.py` module provides SQLAlchemy-based connection management for MySQL 8.0 on Google Cloud SQL.

### Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables (copy `.env.example` to `.env` and fill in your values):
   ```bash
   cp .env.example .env
   ```

3. Configure your environment variables:
   - `DB_USER`: Your MySQL username
   - `DB_PASSWORD`: Your MySQL password  
   - `DB_HOST`: Your Google Cloud SQL host (IP or connection name)
   - `DB_PORT`: MySQL port (default: 3306)
   - `DB_NAME`: Your database name

### Usage

```python
from backend.database import init_db, get_db, Base

# Initialize database connection
init_db()

# Test connection
from backend.database import db_manager
if db_manager.test_connection():
    print("Connected successfully!")

# Use in your application
def get_database_session():
    return next(get_db())
```

### Features

- Connection pooling with QueuePool
- Automatic connection validation (pre_ping)
- Connection recycling (1 hour)
- Proper error handling
- Environment-based configuration
- Session management utilities