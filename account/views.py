from django.contrib.auth import login
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import UserProfile
from .forms import UserRegisterForm, UserProfileForm



class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'transaction/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid

class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'transaction/update_profile.html'
    success_url = reverse_lazy('library:book_list')

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)
