from django.urls import path
from .views import (
    UserRegisterView,
    UserProfileUpdateView,
)
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'account'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', UserProfileUpdateView.as_view(), name='profile'),
]
