# This section is about data relationship
# Connecting Data & Models

# what we learn:
# What are Data Relationship?
# Diffrent type of Relationship
# Managing Relationship with Django Models


# Data commonaly Connected
# In our book project one Book can have only one Author but, one Author can have multiple Books.
# So here two relationship was made. 1.One to One 2.One to Many 
# Also there is 3.Many to Many relationship is there.

# Now we add another "Author" class to models.py file 
# After adding new field first_name and last_name we link Author class to Book class.
# we do this by adding foreign key to the Book class.
# Then Simply run migration.
# After some error solving adding new data to the database.
# And Note that we remove save method which auto generate slug so we need to manualy add that slug for every book.
#   


# In [1]: from book_outlet.models import Book, Author
# In [2]: jk = Author(first_name="J.K.", last_name='Rowlling')
# In [3]: jk.save()
# In [4]: Author.objects.all()
# Out[4]: <QuerySet [<Author: Author object (1)>]>
# In [5]: Author.objects.all()[0].first_name
# Out[5]: 'J.K.'
# In [6]: hp1 = Book(title='Harry Potter 1', rating=5, is_bestselling=True, slug='harry-potter-1', author=jk)
# In [7]: hp1.save()
# In [10]: Book.objects.all()
# Out[10]: <QuerySet [<Book: Harry Potter 1 (5)>]>

# See here IN[6] in author=jk we pass Django automaticaly find the jk indexing in Author Database.

# In [10]: Book.objects.all()
# Out[10]: <QuerySet [<Book: Harry Potter 1 (5)>]>
# In [11]: harrypotter = Book.objects.get(title='Harry Potter 1')
# In [12]: harrypotter
# Out[12]: <Book: Harry Potter 1 (5)>      # IT COMES FROM BOOK MODEL
# In [13]: harrypotter.author
# Out[13]: <Author: Author object (1)>      # IT COMES FROM AUTHOR MODEL
# In [14]: harrypotter.author.first_name
# Out[14]: 'J.K.'
# In [15]: harrypotter.author.last_name
# Out[15]: 'Rowlling'


# CROSS MODEL QUERIES:
# Let's say I want to find all Books where author has last name "Rowlling"
# 
# books_by_rowling = Book.objects.filter(author__last_name="Rowlling")
# In [17]: books_by_rowling
# Out[17]: <QuerySet [<Book: Harry Potter 1 (5)>]>
# In [18]: books_by_rowling = Book.objects.filter(author__last_name__contains="wlling")
# In [19]: books_by_rowling
# Out[19]: <QuerySet [<Book: Harry Potter 1 (5)>]>
# 
# In [20]: jkr = Author.objects.get(first_name='J.K.')
# In [21]: jkr
# Out[21]: <Author: Author object (1)>
# In [22]: jkr.book_set
# Out[22]: <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager at 0x1202b9e86d0>  
# In [23]: jkr.book_set.all()
# Out[23]: <QuerySet [<Book: Harry Potter 1 (5)>]>/
# Remember: FOR NOT WRITE 'book_set' AS REFRENSE WE NEED TO ADD IT TO THE FOREIGN KEY FIELD SECTION IN THE 'related_name' SECTION.
# 
# we set here related_name='books' 
# After added parameter run again migrations.
# 
# In [1]: from book_outlet.models import Book, Author
# In [2]: jkr = Author.objects.get(first_name='J.K.')
# In [3]: jkr.books.all()
# Out[3]: <QuerySet [<Book: Harry Potter 1 (5)>]>
# In [4]: jkr.books.get(title='Harry Potter 1')
# Out[4]: <Book: Harry Potter 1 (5)>
# In [5]: jkr.books.filter(rating__gt=3)
# Out[5]: <QuerySet [<Book: Harry Potter 1 (5)>]>
# 
# Remember:
# jkr.books.all()  Here books is related_name.