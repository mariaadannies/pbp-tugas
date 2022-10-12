from django.urls import path
from .views import toggle_task_finished ,delete_task, logout_user, register, login_user, show_todolist, add_task, show_json, add_new_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('create-task/', add_task, name='add_task'),
    path('delete-task/<int:task_id>/', delete_task, name='delete-task'),
    path('toggle-task/<int:task_id>', toggle_task_finished, name='toggle-task'),
    path('json/', show_json, name='show_json'),
    path('add/', add_new_task, name='add_new_task'),
]