# what include this section:
# Working with templates and static file, Rendering complete pages

# template: Templates will simply be HTML files, which hold HTML code, which can output some dynamic content.

# In this section, we learn about:
# how to render static file like css, javascript, image files
# how to render templates like html files


# For generate the template file:
# go to your app and create folder name as "templates" then again inside templates create "app" name folder and then go inside this folder and create different html file.
#
# Now for correctly render templates goto settings.py file and do changes in "TEMPLATES" name list
# Inside list in "DIRS" list add a path of your templet folder and remember at calling time in views.py file we add like "challenges/challenge.html" so that inside "DIRS" list we do not add "challenges" otherwise we need to add.


# Django has its own templating language which known as DTL(Django Templating Language)
# In if we have standard HTML file, and we add in DTL syntax base code and generate Dynamic HTML page

# DTL language writes inside the: {{ }}

# "Filters":
# Django has a number of filters
# This filter writes in html page and with the symbol of pipe(|)     for example goto challenge.html
# e.g.,
# 1. Basic Filters:
# date, time, datetime, default
# 2. String Filters:
# capfirst, lower, upper, title, truncatewords, truncatechars
# 3. List Filters:
# first, last, length
# 4. Numeric Filters:
# add, divisibleby, floatformat
# and many more...

# "Tags"
# Django supported Tags write inside {% %}
# {% if %}
# {% else %}
# {% elif %}
# {% for %}
# {% empty %}
# {% cycle %}
# {% block %}
# {% extends %}
# {% include %}
# {% load %}
# {% comment %}
# {{ variable }}
# {% with %}
# {% csrf_token %}
# {% form %}
# {% formfield %}
# {% url %}   very important
# {% static %}

# I want to discuss one Tag "Block"
# e.g.,
# {% block page_title %}My Challenges{% endblock %}
# here we write block Tag inside {% %} and we "must" give each block name here it is "page_title"
# and remember we also need to close each block

# Here we add one folder "templates" and there one base.,hyml file inside all blocks is created
# Now we just need to extend this file where we need it but there we if use absolute path like {% extends "../../../templates/base.html"%}
# and in future if =we change the location of file then error is generate for that solution we add template folder in settings.py file
# there ion DIR folder we add relation of template folder which you can see there.


# Accessing Dictionary Fields in Templates
# When accessing dictionary data in a template, you DON'T use this syntax:
# {{ myDictionary['some_key'] }}
# Instead, you use the dot notation - as if it were a regular Python object:
# {{ myDictionary.some_key }}
# This might look strange, but keep in mind, that the DTL is a custom-made language.
# It looks like Python, but ultimately it is NOT Python - it's a language parsed and executed by Django.
# Hence, its syntax can deviate - just as it does here.
# Again, you'll see this in action later in the course!


# Calling Functions in Templates
# Calling functions in templates also works differently than it does in Python.
# Instead of calling it, you use functions like regular variables or properties.
# I.e., instead of:
# {{ result_from_a_function() }}
# you would use
# {{ result_from_a_function }}

# Now we add some css file into it
# for that in-app folder we add static name folder
# and inside also add one more folder same as app name and inside that folder we add static files like css,
# javascript, and image file.

# Note:
# Now go to settings.py file and in "INSTALLED_APPS" see in list "django.contrib.staticfiles" is there or not if it not
# there add in list because if it not there you can't fetch the static file.

# Now Django automatically find static folder and apply css where you {% load static %}
# But the problem is Django can not find static folder at root level means at your project folder(like we create here static name folder at root level like templates)
# we change for templates at the root level identify templates folder in settings.py in DIRS we change or can say add in BASE_DIR list add --> BASE_DIR / 'templates',
# Now for static file

# Example:
# Imagine that you want to build a static URL where some part of the URL (e.g. the filename) is actually stored in a variable that's exposed to the template.
# So you might want to build the URL like this:
# {% static "my_path/to/" + the_file %}
# Here, "the_file" would be a variable holding the actual filename.
# The above code would fail.
# Instead, you can use the "add" filter provided by Django to construct this path dynamically:
# {% static "my_path/to/"|add:the_file %}
