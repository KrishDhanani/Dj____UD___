# blank vs. null:
# blank = True,    when providing a value for this model field(via a form), this field may be blank (empty)
# null = True,     when no value is received for that field, the special NULL value should be store in DataBase.
# if null = False,  You have to ensure that some default value is set in case of blank values.


# Updating Data in Database:
#
# Firstly, write this data in shell
# from book_outlet.models import Book
# code:
# harry_potter = Book.objects.all()[0]
# harry_potter.title    # "Harry Potter 1 - The Philosopher's stone"
# lotr = Book.objects.all()[1]
# lotr.title      # 'Lord Of the rings'
#
#
# Now; if I write in shell and hit enter
# harry_potter.author = 'J.K. Rowling'
# It won't do anything yet, now also write this and hit enter it not do anything,
# harry_potter.is_bestselling = True
# Now,
# harry_potter.save()
# Now if I write upper code and hit enter then it now not generate any new thing in Database, and it just Updates the Database.
# To verify!,
# Book.objects.all()[0].author  # Output: 'J.K. Rowling'


# Delete Data in Database:
# code for shell:
# lotr = Book.objects.all()[1]
# lotr.delete()
# It will delete data from database
# Now if write,
# Book.objects.all()
# It will return: <QuerySet [<Book: Harry Potter 1 - The Philosopher's stone (5)>]>

# create():
# For faster data enter a database, write in shell like
# Book.objects.create(title='Lord Of the Rings', rating=4, author='r.j. shah', is_bestselling=True)
# Book.objects.create(title='My Diary', rating=2, author='k.k. rajkumar', is_bestselling=True)
# Book.objects.create(title='Random', rating=1, author='Random Dude', is_bestselling=False)



# Querying & Filtering Data:
# For getting data on certain condition bases like id = 2 or title = 'Lord Of The Rings' then write like,
# Book.objects.get(title='Lord Of the Rings')   # return: <Book: Lord Of the Rings (4)>
# Book.objects.get(rating=5)
#
# Remember:
# Book.objects.get(is_bestselling=True)
# Then it will return more than one book, and it not handles by get method, get method handle only that query which return single value so pass inside like that query.
#
# for getting multiple value output we use filter()
# write in shell like; Book.objects.filter(is_bestselling=True) # It returns list
#

# And:
# we can also apply "and" condition like;
# Book.objects.filter(is_bestselling=True, rating=2)
# Django check for both condition fulfil items in a database
#
#
# Now if you write like;
# Book.objects.filter(rating<3)    # Django consider it as wrong Syntax for like this condition Django has their own "lookups"(in documentation described) syntax like for write in shell;
# Book.objects.filter(rating__lt=3)    # It considers as lower than
# Book.objects.filter(rating__lte=3)   # It considers as lower than and equal to condition
# Book.objects.filter(rating__lt=5, title__contains='Lord')


# Or:
# in shell first need to import Q class for that:
# from django.db.models import Q
# Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True))  # return list of fulfilling both conditions with, or
#
# also we can combine "and" condition here;
# Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True), Q(author='J.K. Rowling'))


# Query Performance:
# In shell if I write;
# In [11]: bestseller = Book.objects.filter(is_bestselling=True)
#
# In [12]: amazing_bestseller = bestseller.filter(rating__gt=4)
#
# In [13]: print(bestseller)
# <QuerySet [<Book: Harry Potter 1 - The Philosopher's stone (5)>, <Book: Lord Of the Rings (4)>, <Book: My Diary (2)>]>
#
# In [14]: print(amazing_bestseller)
# <QuerySet [<Book: Harry Potter 1 - The Philosopher's stone (5)>]>
#
# In [15]: print(bestseller)
# <QuerySet [<Book: Harry Potter 1 - The Philosopher's stone (5)>, <Book: Lord Of the Rings (4)>, <Book: My Diary (2)>]>
#
# so in input 11 and 12 it's ok to write the query and store in memory but Remember Django is not touch the Database yet
# when you write the print statement and then use inside variable then Django go to Database and now the value is store in
# Django "cashed" and if you see in input 15 again print bestseller then it will execute faster than before because now Django use cashed
# whay this happen because the we already execute this type of query in input 13.
 

# Bulk Operations:
# 1. You can delete multiple model instances (i.e. database records) at once: https://docs.djangoproject.com/en/3.1/topics/db/queries/#deleting-objects

# 2. You can update multiple model instances (i.e. database records) at once: https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-update

# 3. You can create multiple model instances (i.e. database records) at once: https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-create


# Now we all know we not write our database operation in shell at real life project and for that we add new templates in project by simpaly get out of terminal.

# Here we added some html file like base.html(At root level), book_detail.html and index.html(in app), 
# Also config. urls.py at both app as well as main folder.
# Also set setting for root level template file.


# In views.py add data using DataBase:
# Now we add in views.py file models Book class.
# Now you can see the Syntax is same as ago we use in shell for handling data base.
