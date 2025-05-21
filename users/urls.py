from django.urls import path
from .views import RegisterView, UserListCreateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', UserListCreateView.as_view(), name='user-list-create'),
]
