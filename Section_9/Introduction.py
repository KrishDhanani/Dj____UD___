# What include this file:
# User Input, Forms, & Class Based Views
# Using user input & Improving view logic

# Module Content
# Creating & Handling Forms
# Simplifying Form Management
# Exploring Class Based Views

# First we make a form and also add some basic setting to start Django app.

# Now see there if after filing some value inside the input and you hit send button then see browser was reload and also at the url after
# '?' mark whichever value you set to input field it's equal entered value by you display. (like; http://127.0.0.1:8000/?username=hello) 

# so one important thing is whenever you submit any type of form then it was always be a pass with "GET" request and You can see this on browser HEader Section.
# Another method is 'POST'(Collect user data) method which use when we not want to send some data but want get data from server.
# Then we change form method to post then you see in url can't see what use submited
# also getting one error 'forbidden csrf token' 

# CSRF: CROSS SIDE REQUEST FORGEWRIEY
# Let's assume a case where you build one bank website and at money recipient you replace their accoutn number by your and all their money tranfer to your bank account and this is advantage fro attackers; for resolve this type of issue Django comes with csrf tocken.
# So we add a Dynamicaly generated(by us on server) csrf token with our Dynamicaly generated form at submission of form.
# Also token was every time diffrent so no need to wory to see goto inspect and there it is.

# for generate csrf token just goto your form tag and add: {% csrf_token %}

# Handling form submission and extracting data:

