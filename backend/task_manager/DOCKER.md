## Connect to docker
```bash
docker exec -it django_backend bash
python manage.py shell
```

```
from tasks.models import Task, Category
work = Category.objects.create(name="Work", description="Work-related tasks")
task = Task.objects.create(title="Test1", description="Test1")
tasks = Task.objects.all()
print(tasks)
```