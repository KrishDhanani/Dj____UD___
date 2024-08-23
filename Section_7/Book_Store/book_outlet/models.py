from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.name} {self.code}'
    
    class Meta:
        verbose_name_plural = 'Countries'

class Address(models.Model):    #This class helps us in one to one relation ship where one Address can have only onr Author.
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.street}, {self.postal_code}, {self.city}'
    
    class Meta:
        verbose_name_plural = 'Address Entries'
    # This class tell's Django to how this model should output in Admin Pannel.
    # Learn more about it in documentation.
    # For see where the changes is made see at the left corner you see 'Address Entries'.      

class Author(models.Model):     # New added class   # This class help in one to many relationship where one Author and Many Books.
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)       # OneToOneField help us on how data should be the related with each Other.

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'  # In Admin area how Author should look like other wise it shows object.


class Book(models.Model): 
    title = models.CharField(max_length=50)  
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')  # Inside always write that model name with wich we want to pointer at.
    # on_delete=models.CASCADE  It simpaly means if any one of Author deleted then also all the related Book must be deleted. 
    # there also models.PROTECT to not delete book and many others you can refer at Documentation. 
    # Here we add null=True because if already some data we have in book class then want to add some new column then it will run migration for that we need to add it.
    # After solving migrations problem by adding null=True again another problem is accure to run migrate that return error you add two field f_name & l_name but there is already author field inside some value present for existing data
    # Then we remove all data and run migrate command and it succed 
    # Then add some data to Author table and some data to Book table. 

    # ForeignKey: It simply mean to value enter here is simpaly pointer to Author class value enter previouisly.
    
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) 
    
    published_countries = models.ManyToManyField(Country)
    # You can't add on_delete in ManyToMany rel.

    def get_absolute_url(self): 
        return reverse('book-detail', args=[self.slug])  
    

    def save(self, *args, **kwargs):    
        self.slug = slugify(self.title)     
        super().save(*args, **kwargs)    
            
    def __str__(self):
        return f"{self.title} ({self.rating})"
  
