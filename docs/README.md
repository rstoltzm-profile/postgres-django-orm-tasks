# End to end setup
* clone the repo down

## Setup Docker Network
* this will act as our mock environment
```bash
docker network create shared_network
```

## Setup PostgreSQL Container
* this will act as our mock database
```bash
cd backend/database
docker-compose -f docker-compose.db.yml up -d
```
* wait for it to come up then test out pgadmin http://localhost:5050
* register Server in pgadmin. Host name: "postgres_db", port: "5432", user/pass from docker-compose

## Create a database with ansible
* alternatively, you can use pgadmin to create the database
```bash
# from base directory
cd backend/ansible/
# follow README.md to setup ansible
ansible-playbook -i inventory deploy_postgres.yml
```

## Setup the backend ORM
```bash
# from base directory
cd backend/task_manager
docker-compose -f docker-compose.be.yml up -d
```

## Setup the front end
```bash
# from base directory
cd frontend/django_web
docker-compose -f docker-compose.fe.yml up -d
```