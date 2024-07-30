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
# After some error solving(mention in models.py file) adding new data to the database.
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
# In [16]: books_by_rowling = Book.objects.filter(author__last_name="Rowlling")
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
# we set here related_name='books' so although use of 'book_set' we use 'books' from now onwords. 
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
# jkr.books.all()  Here 'books' is related_name.


# See how Author class was register in admin area.
# Now goto admin area after running server.
# There you see I've already added some Author and Books.
# Go one of the Book and see the Author field there you see there a dropdown list is there.
# It means there can be one author can write many books. 
# It clearly shows one to many relationship here.


# Now let's see one to one relationship here.
# We add new class here name as 'Address' which says one author have one Address.
# For one to one relationshio we add OneToOneField in Author class also we add some fields in Adress class.
# Then run migration.
# Here we no need to use related_name because in one to one relationship Django will automatically does it for us.


# Let's learn one to one one relationship here by shell   
# Here first we add some address then assign address to author.
# 
# In [2]: from book_outlet.models import Author, Address, Book
# In [3]: Author.objects.all()
# Out[3]: <QuerySet [<Author: J.K. Rowlling>, <Author: J.R.R. Tolkien Tolkien>, <Author: Raj Patel>]>
# In [5]: Author.objects.all()[0].address
# In [6]: addr1 = Address(street='Some Street', postal_code='12345', city='London')
# In [7]: addr2 = Address(street='Another Street', postal_code='67890', city='New Yourk')
# In [8]: addr1.save()
# In [9]: addr2.save()
# In [10]: jkr = Author.objects.get(first_name='J.K.')
# In [11]: jkr.address
# In [12]: jkr.address = addr1
# In [13]: jkr.save()
# In [14]: jkr.address
# Out[14]: <Address: Address object (1)>
# In [15]: jkr.address.street
# Out[15]: 'Some Street'

# Now reverse
# In [16]: Address.objects.all()
# Out[16]: <QuerySet [<Address: Address object (1)>, <Address: Address object (2)>]>
# In [17]: Address.objects.all()[0].author
# Out[17]: <Author: J.K. Rowlling>
# In [18]: Address.objects.all()[0].author.first_name
# Out[18]: 'J.K.'



# Now One to One Admin pannel.
# See in admin.py how we register Address model and see how the Meta class is work.
# See how to one to one relationship work in admin pannel.
# 


# Let's see Many to Many Relationship.
# Here we set as a Book can pblish on many countries and a country can have many Books.
# For that we add Country class here.
# See in Book class how we added MannyToManyField here.
# 
# Let's see in Shell.
# In [1]: from book_outlet.models import Country, Book
# In [2]: Book.objects.all()
# Out[2]: <QuerySet [<Book: Harry Potter 1 (5)>, <Book: Lord Of the Rings (4)>, <Book: My Story (5)>]>
# In [3]: hp1 = Book.objects.all()[0]
# In [4]: hp1.published_countries
# Out[4]: <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager at 0x20318f85590>
# In [5]: hp1.published_countries.all()
# Out[5]: <QuerySet []>
# In [6]: germany = Country(name='Germany', code='DE')
# In [7]: Book.objects.all()
# Out[7]: <QuerySet [<Book: Harry Potter 1 (5)>, <Book: Lord Of the Rings (4)>, <Book: My Story (5)>]>
# In [8]: mys = Book.objects.all()[2]

# In [9]: mys.published_countries.add(germany)
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# Cell In[9], line 1
# ----> 1 mys.published_countries.add(germany)
# File ~\AppData\Roaming\Python\Python311\site-packages\django\db\models\fields\related_descriptors.py:1201, in create_forward_many_to_many_manager.<locals>.ManyRelatedManager.add(self, through_defaults, *objs)
#    1199 db = router.db_for_write(self.through, instance=self.instance)
#    1200 with transaction.atomic(using=db, savepoint=False):
# -> 1201     self._add_items(
#    1202         self.source_field_name,
#    1203         self.target_field_name,
#    1204         *objs,
#    1205         through_defaults=through_defaults,
#    1206     )
#    1207     # If this is a symmetrical m2m relation to self, add the mirror
#    1208     # entry in the m2m table.
#    1209     if self.symmetrical:
# File ~\AppData\Roaming\Python\Python311\site-packages\django\db\models\fields\related_descriptors.py:1461, in create_forward_many_to_many_manager.<locals>.ManyRelatedManager._add_items(self, source_field_name, target_field_name, through_defaults, *objs)
#    1458     return
#    1460 through_defaults = dict(resolve_callables(through_defaults or {}))
# -> 1461 target_ids = self._get_target_ids(target_field_name, objs)
#    1462 db = router.db_for_write(self.through, instance=self.instance)
#    1463 can_ignore_conflicts, must_send_signals, can_fast_add = self._get_add_plan(
#    1464     db, source_field_name
#    1465 )
# File ~\AppData\Roaming\Python\Python311\site-packages\django\db\models\fields\related_descriptors.py:1377, in create_forward_many_to_many_manager.<locals>.ManyRelatedManager._get_target_ids(self, target_field_name, objs)
#    1375 if isinstance(obj, self.model):
#    1376     if not router.allow_relation(obj, self.instance):
# -> 1377         raise ValueError(
#    1378             'Cannot add "%r": instance is on database "%s", '
#    1379             'value is on database "%s"'
#    1380             % (obj, self.instance._state.db, obj._state.db)
#    1381         )
#    1382     target_id = target_field.get_foreign_related_value(obj)[0]
#    1383     if target_id is None:
# ValueError: Cannot add "<Country: Country object (None)>": instance is on database "default", value is on database "None"

# In [10]: germany.save()
# In [11]: mys.published_countries.add(germany)
# In [12]: mys.published_countries.all()
# Out[12]: <QuerySet [<Country: Country object (1)>]>
# In [13]: mys.published_countries.filter(code='DE')
# Out[13]: <QuerySet [<Country: Country object (1)>]>
# In [14]: mys.published_countries.filter(code='UK')
# Out[14]: <QuerySet []>

# REMEMBER: HERE USED ADD METHOD ONLY AVAILABLE IN MANY TO MANY RELATIONSHOP.

# Now for reverse
#  In [21]: ger = Country.objects.all()[0]
# In [22]: ger.book_set.all()
# Out[22]: <QuerySet [<Book: My Story (5)>]>

# REMEMBER AGAIN WE USE HERE 'book_set' for Book class if you set related_name(in published_country) then specify it here. 


# .........................................
# :::Circular Relations & Lazy Relations:::
# .........................................

# Sometimes, you might have two models that depend on each other - i.e. you end up with a circular relationship.
# Or you have a model that has a relation with itself. 
# Or you have a model that should have a relation with some built-in model (i.e. built into Django) or a model defined in another application.
# Below, you find examples for all three cases that include Django's solution for these kinds of "problems": Lazy relationships. You can also check out the official docs in addition.

# 1) Two models that have a circular relationship:

# class Product(models.Model):
#   # ... other fields ...
#   last_buyer = models.ForeignKey('User')

# class User(models.Model):
#   # ... other fields ...
#   created_products = models.ManyToManyField('Product')
# In this example, we have multiple relationships between the same two models. Hence we might need to define them in both models. By using the model name as a string instead of a direct reference, Django is able to resolve such dependencies.

# 2) Relation with the same model:

# class User(models.Model):
#   # ... other fields ...
#   friends = models.ManyToManyField('self') 
# The special self keyword (used as a string value) tells Django that it should form a relationship with (other) instances of the same model.

# 3) Relationships with other apps and their models (built-in or custom apps):

# class Review(models.Model):
#   # ... other fields ...
#   product = models.ForeignKey('store.Product') # '<appname>.<modelname>'
# You can reference models defined in other Django apps (no matter if created by you, via python manage.py startapp <appname> or if it's a built-in or third-party app) by using the app name and then the name of the model inside the app.

