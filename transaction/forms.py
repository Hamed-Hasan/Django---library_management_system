from django import forms
from .models import Borrow



class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['book']  # Assuming the user is automatically assigned


