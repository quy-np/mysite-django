from django.urls import path
from . import views
from rest_framework import routers

urlpatterns = [
    
    path('', views.ListCreateCarView.as_view()),
    
    path('<int:pk>', views.UpdateDeleteCarView.as_view()),
]