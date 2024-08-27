# In this file we going to create class that defines the shape of our forms and input 
# we wants and the validation rules.

from django import forms
from .models import ReviewModel

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name:", max_length=10, error_messages={
        "required": "Your name must not be empty!", # If this type of error generate then which type of message will show that we does here.
        "max_length": "Please enter a shorter name less than 10 char."
    })
    # Remember Required=True always available in every field.
    # If you not add label then By default Django use its field name(variable name). 

    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea,max_length=200, required=False)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
    # To learn about all form field goto Django Form Field Official Documentation.

class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = ReviewModel     # we instentiate ReviewModel class here
        fields = '__all__'            # here it means all form field ['user_name', 'review-text', 'rating'] but to not write specifically each and every we write like this.
        # exclude = ['user_name']   # It means take all form field but not take user_name field.

        # To see our cutomisable labels 
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

