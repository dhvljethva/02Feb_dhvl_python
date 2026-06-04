from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_list, name='profile_list'),             # home page — list all profiles
    path('create/', views.create_profile, name='create_profile'),  # form page — add a new profile
]
