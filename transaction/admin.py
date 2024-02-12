from django.contrib import admin
from .models import UserProfile, Borrow, Review


admin.site.register(UserProfile)
admin.site.register(Borrow)
admin.site.register(Review)
