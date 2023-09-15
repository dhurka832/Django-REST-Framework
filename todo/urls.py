from django.urls import path 
from . import views

urlpatterns = [
    path('',views.apiOverview,name="api-overview"),
    path('todo-list/',views.TodoList,name="todo-list"),
    path('todo-detail/<str:pk>/',views.TodoDetail,name="todo-detail"),
    path('todo-create/',views.TodoCreate,name="todo-create"),
    path('todo-update/<str:pk>/',views.TodoUpdate,name="todo-update"),
    path('todo-delete/<str:pk>/',views.TodoDelete,name="todo-delete")
]

