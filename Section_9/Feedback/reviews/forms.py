# In this file we going to create class that defines the shape of our forms and input 
# we wants and the validation rules.

from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name:", max_length=10, error_messages={
        "required": "Your name must not be empty!", # If this type of error generate then which type of message will show that we does here.
        "max_length": "Please enter a shorter name less than 10 char."
    })
    # Remember Required=True always available in every field.
    # If you not add label then By default Django use its field name(variable name). 

    # To learn about all form field goto Django Form Field Official Documentation.