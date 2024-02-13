from django.urls import path
from .views import (
    UserRegisterView,
    UserProfileUpdateView,
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='transaction/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='update_profile'),
]
