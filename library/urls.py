from django.urls import path
from .views import BookListView, BookDetailView, ReviewCreateView

app_name = 'library'  # This is for namespacing URLs

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),  # Shows details for a single book
    path('book/<int:pk>/review/', ReviewCreateView.as_view(), name='book_review'),  # Adds a review for a book
]
