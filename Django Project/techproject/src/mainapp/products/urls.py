from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('admin_console', views.admin_console, name='admin_console'),
    path('<int:pk>/details/', views.details, name='details'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('confirmDelete/', views.confirmed, name='confirmed'),
    path('createRecord/', views.createRecord, name='createRecord'),

]
