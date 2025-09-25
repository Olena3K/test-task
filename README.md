Test Task

This application fetches users, addresses, and credit card information from public APIs and stores them in a PostgreSQL database. The tasks are executed periodically using Celery. The project demonstrates clean code, database relationships, Docker containerization, and testing with Pytest.

Features

- Periodic extraction of users from external API.
- Periodic extraction of addresses and credit card data from external API.
- Data is stored in PostgreSQL, with relational links between users, addresses, and credit cards.
- Background task management using Celery with Redis as broker.
- REST API endpoints via FastAPI to fetch users, addresses, and credit cards.
- Fully containerized using Docker.
- Tests using Pytest.
- Linters were not applied, but the code follows standard Python best practices.

Tech Stack
Language & Framework: Python, FastAPI
Database: PostgreSQL
Task Queue / Broker: Celery, Redis
Testing: Pytest
Database ORM & Migrations: SQLAlchemy, Alembic
Containerization: Docker
HTTP Requests: requests
Deployment: ECS, AWS RDS for Postgres, AWS ElastiCache for Redis.

Project Structure
├── app/
│ ├── **init**.py
│ ├── db.py
│ ├── tasks.py
│ ├── celery_app.py
│ ├── api.py
├── tests/
├── Dockerfile
├── docker-compose.yml
├── pytest.ini
├── alembic.ini
├── .env.example
├── requirements.txt
├── .gitignore
└── README.md

Setup Instructions

1. Clone the repository
   git clone https://github.com/Olena3K/test-task.git
   cd test_task
2. Configure environment
   Create a .env file:
   DATABASE_URL=postgresql://postgres:postgres@db:5432/test_task
   REDIS_URL=redis://redis:6379/0
3. Build and run Docker containers
   docker-compose up --build
   This will start:
   PostgreSQL database
   Redis broker
   FastAPI application
   Celery worker for periodic tasks
4. Run tests
   docker exec -it web pytest

API Endpoints
/users/ List users
/users/{user_id}/addresses List addresses for a specific user
/users/{user_id}/creditcards List credit cards for a user

Check API responses via http://localhost:8000/docs/ , http://localhost:8000/users/ , http://localhost:8000/users/1/addresses/ .
