# Test API

## Overview

This is a Flask-based REST API for user authentication. It allows users to register, log in, and retrieve their details using JWT for authentication. The project uses MySQL as the database and is containerized using Docker.

## Prerequisites

Before running the project, ensure you have the following installed:

- **Docker**: Ensure that Docker is installed on your machine. Follow the [Docker installation documentation](https://docs.docker.com/get-docker/) for guidance.
- **Docker Compose**: Docker Compose is typically included with Docker Desktop. Check your version with:
```bash
docker-compose --version
```
- **Python 3.9**

## File Structure

- **Dockerfile**: Defines the Docker image for the Django application.
- **docker-compose.yml**: Configures the services used in the application, including PostgreSQL and Redis containers.
- **run.py**: Script called to run the project
- **.env**: Contains environment variables. This file is not included in the repository for security reasons. Be sure to create one before starting the application.

## Setup

### Step 1: Clone the Repository
```bash
git clone git@github.com:olouwafemiii/Flask-test.git
cd Flask-test
```

### Step 2: Create a `.env`(Environment Variables) file in the `Ethsun` folder with the following content (you can adjust the values as needed):
```env
MYSQL_ROOT_PASSWORD=password
MYSQL_DATABASE=test
MYSQL_USER=yann
MYSQL_PASSWORD=password
SQLALCHEMY_DATABASE_URI=mysql://yann:password@db/test
JWT_SECRET_KEY=your_jwt_secret_key
```

### Step 3: Build and start the containers:
```bash
docker-compose up --build
```

### Step 4: Run migrations:
```bash
docker-compose exec web flask db init
docker-compose exec web flask db migrate -m "Initial migration"
docker-compose exec web flask db upgrade
```

### Step 5. Access the application at `http://localhost:5001`.

## API Endpoints : Use Postman or curl to test the endpoints

- **POST /auth/register**: Register a new user by providing the "Email" and the "Password".
- **POST /auth/login**: Authenticate a user and obtain a token by providing the "Email" and the "Password" used to register.
- **GET /users/me**: Get User's Info by providing the token received previously in the Header.

## Running Unit Tests

To run the unit tests for the application, use the following command in the bash terminal:

```bash
docker-compose exec web pytest
```

This command will execute the tests defined in the project using pytest within the Docker container.

---
