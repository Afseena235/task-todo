
from django.urls import path
from .views import ToDoApiView, ToDoDetailApiView

app_name = 'api_v1_todo_list'

urlpatterns = [
    path('', ToDoApiView.as_view(), name='todo_list_create'),
    path('details/<int:pk>/', ToDoDetailApiView.as_view(), name='todo_detail'),
]

