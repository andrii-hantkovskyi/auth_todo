from django.urls import path

from main.views import logout_view, login_view, register_view, index, add_todo, remove_todo

urlpatterns = [
    path('', index, name='home'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('add-todo/', add_todo, name='add-todo'),
    path('remove-todo/<int:todo_id>', remove_todo, name='remove-todo')
]
