from django.db import models


# Create your models here.
class Book(models.Model):   # in models Model is class
    title = models.CharField(max_length=50)     # max_length is required argument
    rating = models.IntegerField()

# Here for getting a different type of field, go to the Django documentation Field section.
