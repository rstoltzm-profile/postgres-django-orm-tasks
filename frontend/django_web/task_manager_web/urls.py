from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:task_id>/', views.delete_task_view, name='delete_task'),
]
