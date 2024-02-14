
from django.urls import path
from .views import (
    BorrowBookView,
    BorrowListView,
    return_book,
)
app_name = 'transaction'
urlpatterns = [
    path('borrow/', BorrowBookView.as_view(), name='borrow_book'),
    path('borrow/list/', BorrowListView.as_view(), name='borrow_list'),
    path('return/<int:pk>/', return_book, name='return_book'),
    path('borrow/<int:book_id>/', BorrowBookView.as_view(), name='borrow_book'),

]
