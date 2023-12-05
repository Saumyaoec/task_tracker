from django.urls import path

from .views import *

urlpatterns = [
    path('',TaskListHomeView.as_view(), name = 'task_list'),
    path('addtask/', TaskAddView.as_view(), name = 'add_task'),
    path('updatetask/<int:pk>/', TaskUpdateView.as_view(), name = 'update_task'),
    path('deletetask/<int:pk>/', TaskDeleteView.as_view(), name = 'delete_task')
]