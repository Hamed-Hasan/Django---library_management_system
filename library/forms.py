
from django import forms
from transaction.models import Review
from .models import Book, Category

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content',]



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'image', 'borrowing_price', 'categories']



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
