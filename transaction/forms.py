

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Borrow, UserProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['book']  # Assuming the user is automatically assigned

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['balance']
