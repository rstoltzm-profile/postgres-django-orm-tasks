# task_manager

## Docker
```bash
docker-compose -f docker-compose.be.yml up -d
```

## Rebuild
```bash
docker-compose -f docker-compose.be.yml down
docker-compose -f docker-compose.be.yml build
docker-compose -f docker-compose.be.yml up -d
```

## Test ORM
```bash
python3 manage.py shell
```

```python
task = Task.objects.create(title="Finish report", description="Complete the quarterly report", category=work)

# Query tasks
tasks = Task.objects.all()
print(tasks)
# Create a task
task = Task.objects.create(title="Test", description="Test, category=work)

# Query tasks
tasks = Task.objects.all()
print(tasks)
```