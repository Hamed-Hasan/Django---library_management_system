from django.db import models
from django.conf import settings
from library.models import Book


class Borrow(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='borrows')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrows')
    borrowed_on = models.DateTimeField(auto_now_add=True)
    returned_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} borrowed {self.book.title}'

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} on {self.book.title}'
