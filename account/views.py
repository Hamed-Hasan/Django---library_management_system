from django.contrib.auth import login
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import UserProfile
from .forms import UserRegisterForm, UserProfileForm



class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        valid = super().form_valid(form)  # This saves the User model
        UserProfile.objects.create(user=self.object)  # Create UserProfile for the new user
        login(self.request, self.object)  # Log in the newly created user
        return valid

    form_class = UserRegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid

class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'account/profile.html'
    success_url = reverse_lazy('library:book_list')

    def get_object(self, queryset=None):
        obj, created = UserProfile.objects.get_or_create(user=self.request.user)
        return obj

