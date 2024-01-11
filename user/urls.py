# myapp/urls.py
from django.urls import path
from .views import (
    UserListCreateView,
    UserRetrieveUpdateDestroyView,
    UserConfigurationListCreateView,
    UserConfigurationRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('user-configurations/', UserConfigurationListCreateView.as_view(), name='user-configuration-list-create'),
    path('user-configurations/<int:pk>/', UserConfigurationRetrieveUpdateDestroyView.as_view(), name='user-configuration-detail'),
]