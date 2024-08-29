from django import forms

class ProfileForm(forms.Form):
    user_image = forms.ImageField()  
    # FileField help to upload File.
    # ImageField help to upload Image.(Only accept Image fiel No pdf document for example)