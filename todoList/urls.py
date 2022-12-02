from django.urls import path
from todoList import views
from .models import Todo

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.add, name="add"),
    path('update/<int:task_id>', views.update, name="update"),
    path('delete/<int:task_id>', views.delete, name="delete"),
    path('search', views.search, name="search")
]