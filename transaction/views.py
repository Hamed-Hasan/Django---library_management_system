from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import  Borrow
from account.models import  UserProfile
from .forms import  BorrowForm
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class BorrowBookView(LoginRequiredMixin, CreateView):
    model = Borrow
    form_class = BorrowForm
    template_name = 'transaction/borrow_book.html'
    # Redirect to the book list page if the book is borrowed successfully
    success_url = reverse_lazy('library:book_list')

    def form_valid(self, form):
        try:
            # Get the user profile to check the balance
            user_profile = UserProfile.objects.get(user=self.request.user)
            book = form.cleaned_data['book']

            # Check if the user's balance is sufficient to borrow the book
            if user_profile.balance >= book.borrowing_price:
                # Deduct the borrowing price from the user's balance
                user_profile.balance -= book.borrowing_price
                user_profile.save(update_fields=['balance'])

                # Create the Borrow object
                borrow = form.save(commit=False)
                borrow.user = self.request.user
                borrow.save()

                # Add a success message
                messages.success(self.request, 'You have successfully borrowed the book.')
            else:
                # Add an error message
                messages.error(self.request, 'You do not have enough balance to borrow this book.')
                return self.form_invalid(form)

        except UserProfile.DoesNotExist:
            # Add an error message
            messages.error(self.request, 'User profile not found.')
            return self.form_invalid(form)

        return super().form_valid(form)

    def form_invalid(self, form):
        # Add an error message
        messages.error(self.request, 'There was an error borrowing the book.')
        return super().form_invalid(form)

    def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            if 'request' in kwargs:  # Ensure that 'request' is actually in kwargs
                self.request = kwargs['request']
            return kwargs

    def get_success_url(self):
        # Redirect to the book detail page after borrowing
        book_id = self.object.book.id
        return reverse_lazy('library:book_detail', kwargs={'pk': book_id})

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
