from django.contrib.auth import login
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import  Borrow
from account.models import  UserProfile
from .forms import  BorrowForm
from django.shortcuts import redirect
from django.utils import timezone


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
