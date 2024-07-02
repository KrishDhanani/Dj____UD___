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

