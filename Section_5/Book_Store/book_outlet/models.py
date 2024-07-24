from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


# Create your models here.
class Book(models.Model):  # in models Model is class (we extend class here)
    title = models.CharField(max_length=50)  # max_length is required argument
    
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    author = models.CharField(null=True, max_length=100)
    # here null=True means if the entries are not inserted, then automatically set to Null.
    # if you do here blank= True, then it does not place any values like Null, it just lives that entire blank
    is_bestselling = models.BooleanField(default=False)


    # Here for getting a different type of field, go to the Django documentation Field section.

    def get_absolute_url(self): # It's Override method which simply return path for all book. 
        return reverse('book-detail', args=[self.id])   
            
    def __str__(self):
        return f"{self.title} ({self.rating})"
