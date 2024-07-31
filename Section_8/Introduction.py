# What we do in this Section:
# Project Building a Blog: Applying what we learned Thus Far
#  
# Defining our Data/Model Requirement
# Adding Model & Relationship
# Adjusting Views & Templates


# In this Module we convert all dumy data to database.
# For see which are the dummy data are for that goto Section_4/views.py file and see.

# Our Blog Data Sample.
# Here we create total 3 models.
# 1.Author 2.Post 3.Tag
# 
# 1.Author:
# First_name
# Last_name
# E-mail_Address
# 
# 2.Post
# Title
# Excerpt
# Image Name
# Date 
# Slug
# Content
# 
# 3.Tag
# Caption
# 
# Here Between Author and Post, One to Many relationship was there.
# And Between Post and Tag Many to Many relationship was there.
# 

# Firstly we add all the models and also all relation in it.
# Then now register all the models in admin.py file to see on admin pannel.
# Then run migration.
# Then we create superuser (in my case name:krish email:abc@gmail.com password:123456)
# Then after login by using admin pannel add all post related data and also add author and tag there.(For select multiple tag hold ctrl and select whichever you want)
# Then add fielter and display section by admin.py file using.
# Then by title we add automaticaly adding slug field.

# Now Fetching data from Database and add to relavent use in view.py see that. 