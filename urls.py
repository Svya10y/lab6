from django.contrib import admin
from django.urls import path, re_path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.archive, name='archive'),
    path('task/new/', views.create_task, name='create_task'),
    re_path(r'^task/(?P<task_id>\d+)$', views.get_task, name='get_task'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
