from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("query_all/", views.get_all_tasks, name="get all tasks"),
    path("query/<str:title>", views.get_task, name="get task by title"),
    path("new/", views.create_task, name="new task"),
    path("delete/<str:title>", views.delete_task, name="delete task by title"),
    path("delete_all/", views.delete_all_tasks, name="delete all tasks"),
]
