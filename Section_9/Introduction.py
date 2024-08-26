# What include this file:
# User Input, Forms, & Class Based Views
# Using user input & Improving view logic

# Module Content
# Creating & Handling Forms
# Simplifying Form Management
# Exploring Class Based Views

# So till now whichever data we are inserted through admin pannel is for only owner of that website for insert from user data we need forms.

#  So first we make a form and also add some basic setting to start Django app.

# Run Code.
# Now see there if after filing some value inside the input and you hit send button then see browser was reload and also at the url after
# '?' mark whichever value you set to input field it's equal entered value by you display. (like; http://127.0.0.1:8000/?username=hello) 

# so one important thing is whenever you submit any type of form then it was always be a pass with "GET" request and 
# You can see this on browser Header Section to see it goto networks and header section in your browser.
# Another method is 'POST'(Collect user data) method which use when we not want to send some data but want get data from server.
# Then we change form method to post then you see in url can't see what user submited
# also getting one error 'forbidden csrf token' 

# CSRF: CROSS SIDE REQUEST FORGEWRIEY
# Let's assume a case where you build one bank website and at money recipient you replace their accoutn number by your and all their money tranfer to your bank account and this is advantage fro attackers; for resolve this type of issue Django comes with csrf tocken.
# So we add a Dynamicaly generated(by us on server) csrf token with our Dynamicaly generated form at submission of form.
# Also token was every time diffrent so no need to wory to see goto inspect and there it is.

# for generate csrf token just goto your form tag and add: {% csrf_token %}
# So the conclution is whenever yu submitt the data in form using post method need to add csrf tocken.



# Handling form submission and extracting data:
# So here at the time of form submission to transfer from http://127.0.0.1:8000/ to http://127.0.0.1:8000/ we add action attribute in form tag.
# Here we add just '/' if we added '/add-on' then it will redirect to http://127.0.0.1:8000/add-on/
# So we want to capture data so first we identify by which request(GET/POST) using the form was submitted.
# Then take require action. Here we simply on submiting form render thank you page.
 

# Manually form validation and problem with "that":
# If there is nothing written inside the form and user submit form then we want to show some error news 
# Handling form validation is typically very lenthy task i added one example here. 
# To resolve it Django has it's own Form Class. 


# Using Django Form Class:
# For this part understand first goto forms.py file

# Validation using Django form 
# again see in the forms.py file

# Coustomizing form Control like adding label and etc.
# Then
# TO show not full form at once means to show where the form field look and where the error nessage show for 
# goto the review.html
#  

# By using inspect you can see when error was generate than by Django there is "errorlist" class was generated inside unordered list.
# here by using that class we add some css to the form.

# Then we storing form data to the database.
