from django.contrib import admin
from .models import Category, User, Item

# TODO: 2 for admin testing
admin.site.register(Category)

admin.site.register(User)

admin.site.register(Item)