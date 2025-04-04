from django.shortcuts import render, redirect
from .api_service import get_tasks, create_task, delete_task

def home(request):
    if request.method == "POST":
        # Handle task creation
        title = request.POST.get("title")
        description = request.POST.get("description")
        create_task(title, description)
        return redirect("home")

    # Fetch tasks from the backend
    tasks = get_tasks()
    return render(request, "home.html", {"tasks": tasks})

def delete_task_view(request, task_id):
    if request.method == "POST":
        delete_task(task_id)
        return redirect("home")