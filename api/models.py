from django.db import models

# TODO: 1 for sql models
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# python manage.py runserver
# python manage.py flush --for resetting the database

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)
    condition = models.CharField(max_length=50)
    description = models.TextField()
    security_deposit = models.FloatField()
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='users')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='items', null=True)


    def __str__(self):
        return self.name
