Steps to Get Started:
1. Set Up PostgreSQL Container:
Create a Docker container for PostgreSQL.
Configure the database and create necessary tables.

```
docker-compose -f docker-compose.db.yml up -d
docker-compose -f docker-compose.db.yml down
```

2. Backend Development:
Set up Django project and app.
Implement user authentication using Django's built-in auth system.
Create models for tasks and categories using Django ORM.
Develop views and APIs for task management.

```
docker-compose.backend.yml up -d
```

## Need Shared network
```
docker network create shared_network
```