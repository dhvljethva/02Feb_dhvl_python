
from django import views
from django.contrib import admin
from django.urls import path, include
from djangoapp import views

urlpatterns = [
   path('',views.index),
   path('showdata/',views.showdata),
   path('deletedata/<int:id>',views.deletedata),
   path('updatedata/<int:id>',views.updatedata)
]