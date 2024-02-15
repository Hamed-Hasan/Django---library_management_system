from django.urls import path
from .views import BookListView, BookDetailView, ReviewCreateView, BookCreateView, CategoryCreateView

app_name = 'library'  # This is for namespacing URLs

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),  # Lists all books
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),  # Shows details for a single book
    path('book/<int:pk>/review/', ReviewCreateView.as_view(), name='book_review'),  # Adds a review for a book
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
]
