from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Book
from transaction.models import Review
from .forms import ReviewForm

class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'library/add_review.html'
    success_url = reverse_lazy('library:book_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book_id = self.kwargs['pk']
        return super().form_valid(form)
