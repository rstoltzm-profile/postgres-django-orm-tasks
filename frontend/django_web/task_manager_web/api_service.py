import requests

BASE_API_URL = "http://backend:8000/api"

def get_tasks():
    """Fetch all tasks from the backend API."""
    response = requests.get(f"{BASE_API_URL}/tasks/")
    response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
    return response.json()

def create_task(title, description):
    """Create a new task via the backend API."""
    payload = {
        "title": title,
        "description": description
    }
    print("Payload being sent to backend:", payload)  # Debugging log
    response = requests.post(f"{BASE_API_URL}/tasks/", json=payload)
    response.raise_for_status()
    return response.json()

def delete_task(task_id):
    """Delete a task via the backend API."""
    url = f"{BASE_API_URL}/tasks/{task_id}/"
    response = requests.delete(url)
    response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
    print(f"Task with ID {task_id} deleted successfully.")  # Debugging log
    return response.status_code  # Return the status code for confirmation