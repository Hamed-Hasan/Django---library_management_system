from django.contrib.auth import login
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import UserProfile
from .forms import UserRegisterForm, UserProfileForm
from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings

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

class UserProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'account/profile.html'
    success_url = reverse_lazy('library:book_list')
    success_message = "Your profile was updated successfully, and a confirmation email has been sent."

    def form_valid(self, form):
        response = super().form_valid(form)
        # Send email if there's a change in the balance
        if 'balance' in form.changed_data:
            user = self.object.user
            send_mail(
                subject='Balance Update Confirmation',
                message=f'Dear {user.username},\n\nYour new balance is {self.object.balance} Taka.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )
            # print(user.email)
        return response

    def get_object(self, queryset=None):
        # This assumes that a UserProfile instance already exists for each user.
        return self.request.user.userprofile
