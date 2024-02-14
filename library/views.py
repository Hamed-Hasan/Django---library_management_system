from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Book, Category
from transaction.models import Review
from .forms import ReviewForm

class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(categories__name=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context



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
