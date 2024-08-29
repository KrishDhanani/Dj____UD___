from django.db import models

# Create your models here.

class UserProfile(models.Model):
    # image = models.FileField(upload_to='images')
    # FileField use is very bad practice to use in model because it do slow our website 
    # Here uploaded file will not store in database
    # insted it store file in our hard-drive somewhere and it just store file path insted of full file.

    # Here written upload_to meaning store File in setting.py file MEDIA_ROOT alocated folder inside 'images' fodler.

    image = models.ImageField(upload_to='images')
    # The idea is same as file field but it just now accept image file no pdf and any other formate.
