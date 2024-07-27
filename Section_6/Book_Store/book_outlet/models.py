from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Book(models.Model):  # in models Model is class (we extend class here)
    title = models.CharField(max_length=50)  # max_length is required argument
    
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    author = models.CharField(null=True, max_length=100)
    # here null=True means if the entries are not inserted, then automatically set to Null.
    # if you do here blank= True, then it does not place any values like Null, it just lives that entire blank
    is_bestselling = models.BooleanField(default=False)

    slug = models.SlugField(default="", blank=True, null=False, db_index=True) # if title is Harry Potter 1 => harry-potter-1
    # for finding faster slug in database we use db_index=True
    # Here for getting a different type of field, go to the Django documentation Field section.


    def get_absolute_url(self): # It's Override method which simply load the data for this specific model. 
        return reverse('book-detail', args=[self.slug])  # Before there is self.id is there. 
    

    def save(self, *args, **kwargs):     # It is built in method which we override here
        self.slug = slugify(self.title)     # conver Book_title to slug
        # before next line written save method specify which you want to convert in slug formate. 
        super().save(*args, **kwargs)    # Need to always write for run built in save method.  
            
    def __str__(self):
        return f"{self.title} ({self.rating})"
  
