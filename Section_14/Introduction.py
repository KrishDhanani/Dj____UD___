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
# 
# After making it Successfully need to activate it. 
# But In out System there is Policy eror accure to resolve: goto Powershell, 
# (We run it also in terminal but i do first time in cmd so path are like that...)
# PS C:\Users\Krish> Get-ExecutionPolicy
# Ans: Restricted
# PS C:\Users\Krish> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass     (Temporary Deactivate)
# PS C:\Users\Krish> cd..
# PS C:\Users> cd..
# PS C:\> cd My
# PS C:\My> cd learning
# PS C:\My\learning> cd Dj____UD___
# PS C:\My\learning\Dj____UD___> cd Section_14
# PS C:\My\learning\Dj____UD___\Section_14> cd my_site
# PS C:\My\learning\Dj____UD___\Section_14\my_site> .\django_my_site\Scripts\Activate.ps1
# (django_my_site) PS C:\My\learning\Dj____UD___\Section_14\my_site>
# 
# Now again install Django & Pillow library here:
# (django_my_site) PS C:\My\learning\Dj____UD___\Section_14\my_site> python -m pip install Django Pillow 
# 
# Again write this commmand:
# python -m pip freeze > requirements.txt   (Now this file contain really just which Project needs)
# 
# To know about more virtual env: https://docs.python.org/3/library/venv.html#creating-virtual-environments
# 
# We write this commands in Settings.py
# from os import getenv
# DEBUG = getenv("IS_PRODUCTION", True)
# ALLOWED_HOSTS = [
#     getenv("APP_HOST")  # NAME IS UPTO YOU
# ]
# 
# We set this two variable here we can also set SECRET_KEY and it important to set in SECRET_KEy if you upload your code to github.


# We use here AWS:
# For that U need to have AWS acc.
# After that go to(search) for server "Elastic Beanstalk".
# Then goto "Create Application".
# In Application Information add "any name".
# In platform select for "Python".
# in application code select for "Upload your code".
# Now in Our project add one folder name as ".ebextensions"
# Now in this folder we need to add file name as "django.config" (Make sure there is no "typos" in your file)
# Now create all project zip file.
# After upload it in application code.
# After in Presents click on "Single instance".

