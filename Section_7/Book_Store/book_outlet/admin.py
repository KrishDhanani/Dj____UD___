from django.contrib import admin

from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):      # write your model name follow with Admin and "A" in uppercase. 
    # readonly_fields = ("slug",)    #It's tuple   # Using this you can see that which field are read only field there. 
    prepopulated_fields = {"slug": ('title',)}
    # If you write this line our slug field you can see it but remember can't enter any value just see which slug is generated.

    # Now for filter are at side of All Books
    list_filter = ("author", "rating")

    # How all Book seen us, to decide like which field only show
    list_display = ("title", "author") 

admin.site.register(Book, BookAdmin)