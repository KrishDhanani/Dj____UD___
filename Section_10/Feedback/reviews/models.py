from django.db import models

# Create your models here.

class ReviewModel(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()        # We use here TexField and in form we use CharField
    rating = models.IntegerField()