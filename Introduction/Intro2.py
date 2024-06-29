# How to add Django pre require file
# First go to "Command Prompt"
# Now change to that directory where you want to create the folder with essential file of Django
# Now write code:
# python -m django startproject folder_name

# That's it now go to your file explorer you can see some file are automatically there which you not generated.
# This was happen by Django-Admin.

# Now there you see there is "5" Different file are there:
# 1. __init__.py:  
# This file firstly empty and it use to import module and Packages.
# 2. asgi.py & wsgi.py:
# Just don't touch this file's we change in this file's at the deployment time period. This file help to serving our django application.
# 3. settings.py:
# This file contains bunch of pre recrusite settings. We come time to time and change according to we need some type of feature and certain behavior.
# 4. urls.py: 
# This file is important and use when we add more and more Web pages to our website.

# And then we add our custom file.


# For run the server the code is:
# python manage.py runserver
