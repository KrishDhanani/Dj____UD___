# Deploying Django Website
# From Devlopment To Production

# Module Content 
# Deployment Consideration & Pitfall
# Deploying our Blog Website

# Deployment Consideration:
# Choose Database

# Also see pdf uploaded here
# To se SQL VS No-SQL Comarision: https://academind.com/tutorials/sql-vs-nosql/

# To know what are diffrence in between WSGI and ASGI goto official documentation and see in Deploying Section.
# Most Commanly WSGI is used.


# See in PDF 4th page.
# Static Files and User Uploads are not searver by Django automatically.
# For that many option are available:
# 1.Add in urls.py file ::: " + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) "  (It is not perfoemance optimal)
# 2.Configure web server to serve static file AND Django app 
# 3.Use dedicated service/serve for static and uploaded file's


# Choosing Hosting Provider:
# Here we use AWS Hosting Provider.

# We set Debug to False.
# Here uploaded file is also after uploding detect as static file.  
# Also add STATIC_ROOT field in Settings.py
# Also don't forget collect all the static file to new folder.

# Todo 1st approach just add in main folder urls.py file add (bUT REMEMBER this is for lightly usage where not very high traffic accur)
# go that file: static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# 
# Also again run migrations to ensure all migrate happen corectly.
# Also don't forget to createsuperuser.
# 
# Let's prepare for Deployment.
# Write this command to add requirements(dependecy list)
# python -m pip freeze > requirements.txt
# You see there is also unnecesary item which not related to our project.
# 
# for that we create virtual environment:
# to create new virtual env.
# python -m venv django_my_site  