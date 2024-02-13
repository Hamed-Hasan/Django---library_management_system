
from django import forms
from transaction.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content',]
