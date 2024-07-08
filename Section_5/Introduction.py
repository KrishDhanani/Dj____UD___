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



