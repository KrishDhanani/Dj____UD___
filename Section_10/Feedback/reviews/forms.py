# In this file we going to create class that defines the shape of our forms and input 
# we wants and the validation rules.

from django import forms
from .models import ReviewModel

class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = ReviewModel     
        fields = '__all__'           

        labels = {
            'user_name': "Your Name",
            'review_text': "Your Feedback",
            'rating': "Your Rating" 
        }
        error_message = {
            'user_name': {
                "required": "Your name must not be empty!", 
                "max_length": "Please enter a shorter name less than 10 char."
            }
        }

