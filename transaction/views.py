from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from .models import UserProfile, Borrow
from .forms import UserRegisterForm, UserProfileForm, BorrowForm
from django.shortcuts import redirect
from django.utils import timezone

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

class BorrowBookView(CreateView):
    model = Borrow
    form_class = BorrowForm
    template_name = 'transaction/borrow_book.html'
    success_url = reverse_lazy('transaction:borrow_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        # Deduct the borrowing price from user's balance
        book_price = form.cleaned_data['book'].borrowing_price
        user_profile = UserProfile.objects.get(user=self.request.user)
        user_profile.balance -= book_price
        user_profile.save()
        return super().form_valid(form)

class BorrowListView(ListView):
    model = Borrow
    template_name = 'transaction/borrow_list.html'
    context_object_name = 'borrows'

    def get_queryset(self):
        return Borrow.objects.filter(user=self.request.user)

# Assuming a function-based view for simplicity in returning books
def return_book(request, pk):
    borrow = Borrow.objects.get(pk=pk, user=request.user)
    # Add the borrowing price back to user's balance
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.balance += borrow.book.borrowing_price
    user_profile.save()
    borrow.returned_on = timezone.now()  # Ensure you import timezone
    borrow.save()
    return redirect('transaction:borrow_list')
