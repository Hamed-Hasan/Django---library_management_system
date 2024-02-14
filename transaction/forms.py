
from django import forms
from .models import Borrow

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['book']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

