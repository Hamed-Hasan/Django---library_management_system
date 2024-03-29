from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Book, Category
from transaction.models import Review
from .forms import BookForm,CategoryForm,ReviewForm




class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'library/category_create.html'
    success_url = reverse_lazy('library:book_list') 

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_create.html'
    success_url = reverse_lazy('library:book_list')

class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'
    paginate_by = 6  # Display 6 books per page

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
