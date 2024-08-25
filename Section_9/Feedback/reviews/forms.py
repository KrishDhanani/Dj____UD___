# In this file we going to create class that defines the shape of our forms and input 
# we wants and the validation rules.

from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField()