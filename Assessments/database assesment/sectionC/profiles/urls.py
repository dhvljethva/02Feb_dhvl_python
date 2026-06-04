from django.urls import path
from . import views

# Clean URL routing for List, Create, Edit, and Export views
urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('create/', views.profile_create, name='profile_create'),
    path('edit/<int:pk>/', views.profile_edit, name='profile_edit'),
    path('export/', views.profile_export, name='profile_export'),
]
