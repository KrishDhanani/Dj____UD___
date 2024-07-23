# In this Section, we learn about:
# Working with Data, Databases, & Models
# Storing Data in A Persistent Way

# Module Content:
# What is "Data" and "Database"?
# Exploring SQL & Models
# Django, Models & Database Queries

# What is Data:
# It has three categories; Temporary Data, Semi-Persistent Data, Persistent Data
#
# 1. Temporary Data:
# e.g., User Input, Selected Blog Post
# Data is used immediately and lost after
# Store in Memory (Variable)
#
# 2. Semi-Persistent Data:
# e.g., User Authentication Status (in login form after login the data was deleted from form field)
# Data is stored for a longer time but may be lost(can be recreated)
# Store in Browser, Temporary Files
#
# 3. Persistent Data:
# e.g., Blog Posts, Order...
# Data is Store forever and must not be lost
# Store in Database

# Databases:
# There are two fundamental approaches to store data in database
# SQL and NoSQL
# SQl: (It stores data like a table form)
# Table-Based, e.g., MySql, PostgresSQL, SQLite
# NoSQL: (It stores data like Dictionary Form)
# Document-Based, e.g., MongoDB, CassandraDB

# Understanding SQl Queries for general info. It doesn't use in Django because Django hase Model:
# Create table & set table schema (Only done once, when DB is initiated):
# CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT,
#   title TEXT NOT NULL,
#   rating INTEGER NOT NULL)
#
# Insert Data into Table:
# INSERT INTO books (title, rating) VALUES ('Lord Of Rings', 5)
#
# Get Data From table(possible with condition):
# SELECT * FROM books WHERE rating > 5

# Role Of Django Model:
# Focus on your Data not on the queries
# Define Data models and use an object based on those models to run a common operation
# Django model translate instructions (written with python) to SQL queries


# we add our database tabel(model) related information inside app in models.py file
# Now for Django to aware our database, inside app migration folder,
# And before run any model we need to always ensure run or assign first migration.
# for that got to at project level in your terminal
# Code:
# python manage.py makemigrations
# So run this command every time whenever you do changes in models.py file in app

# Now
# run in project level in terminal code:
# python manage.py migrate
# this command executes all Installed app's migration files that created by upper side and by default Django

# Conclusion:
# Firstly, we add all our requirement in our app's models.py folder then run migrations command so some file was generated in-app migration folder then run migrate command to execute all migration files.
# Remember:
# In Django you don't need to create a specific column for id, Django automatically creates that column
# You always need to perform migration whenever you try to change in models.py file inside any class you add or modify any field.



# Inserting Data:
# After migrate for insert data we goto shell in the terminal
# For that first goto at project level in your terminal
# write code: python manage.py shell
#
# Now we import Book class from models.py file for that write in she'll
# write code: from book_outlet.models import Book
#
# Now we need to create object of class which data we need to insert
# write code: harry_potter = Book(title="Harry Potter 1 - The Philosopher's stone", rating=5)
# Remember this upper line not touch database we simply create object and need to remember need to pass keyword argument
#
# Now Django has built in function save() which help to store data in database
# write code: harry_potter.save()
#
# let's store another data
# write code: lord_of_the_ring = Book(title="Lord Of the rings", rating= 4)
# write code: lord_of_the_ring.save()
#
#
#
#
#
# Fetching Data:
# For get all Entries --> class_name.objects.all()
# e.g.,  Book.objects.all()     # return: <QuerySet [<Book: Book object (1)>, <Book: Book object (2)>]>


# Updating Models and Migrations:
# 1. def __str__():     # This method is not Django specific it is built-in method in any class
# -> goto models.py file and see __str__ function in which return line say's whenever class output generates,
#    generate output string as specified formate.
#

# Now to see output in "readable" form restart shell
# So,
# for that need to close the terminal and restart it
# and remember to go project level in the terminal and then write this code:
# in terminal: python manage.py shell
# in shell: from book_outlet.models import Book
# in shell: Book.objects.all()
#



# Validators: # For more info goto Django official Documentation "Validator Section"
# in Models.py file first we import the validator then add some validator see in rating.

# Also we add two new field name: author, is_bestselling
# So now we add two new column we need to register it to our schema so, ...
#
#
# for get out from shell: ctrl + D
#
# Now, ensure your terminal at project level and write code:
# python manage.py makemigrations
#
# try to understand what Django tell you in two option:
# it say before you added entries not have any data for new column and entries not nullable fill there then which option you choose
# I choose here 2nd option (It mean's quit the migration and I need to manually add default value to new added field).
# So that need to models.py file and add manually default value in field.
#
# After do changes like if user not provided any value for any particulate field then what Django needs to do,
# now just re-run the code of migrations
#
#
# That's it for see it does or not goto app migration folder
# and see if there is any type of new file is generated or not which include which are the changes done by your side.
#
#
# Now to run this migration
# Code: python manage.py migrate

# To see the output open shell then:
# code:
# from book_outlet.models import Book
# Book.objects.all()[1]    # to access the first item
# Book.objects.all()[1].author  # using dot notation we can access for particular column entry
# Book.objects.all()[1].rating  # output: 4

