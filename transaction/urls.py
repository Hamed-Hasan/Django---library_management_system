# transaction/urls.py

from django.urls import path
from .views import (
    UserRegisterView,
    UserProfileUpdateView,
    BorrowBookView,
    BorrowListView,
    return_book,
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='transaction/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='update_profile'),
    path('borrow/', BorrowBookView.as_view(), name='borrow_book'),
    path('borrow/list/', BorrowListView.as_view(), name='borrow_list'),
    path('return/<int:pk>/', return_book, name='return_book'),
]
