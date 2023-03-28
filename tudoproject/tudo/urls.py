from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate,TaskDelete,TaskDetail
from . import views

from django.contrib import admin
urlpatterns=[
    path('task-list',TaskList.as_view(),name='task'),
    path('task-create',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
    path('task-detail/<int:pk>/',TaskDetail.as_view(),name='task-detail'),
    path('',views.index, name="index"),
    path('signin/',views.signin, name="signin"),
    path('signup/',views.signup, name="signup"),
    path('details/',views.details,name="details"),

]

















