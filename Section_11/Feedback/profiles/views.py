from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.

# # This is code we can write by our own self when we write usinf form tag in template folder to store file another method is to using Django functionality in forms.py file.
# def store_file(file):       # Inside writen code is run in over all main folder so we create folder at inside main project folder.
#     with open('temp/image.jpg', 'wb+') as dest:     # wb+ means we store in binary way
#         for chunk in file.chunks():         # we insted use .read() but if our file was to much big then Documentation suggest us to use chunks().
#             dest.write(chunk)


# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             'form': form,
#         })

#     def post(self, request):
#         # print(request.FILES['image'])       # Which give us access toi uploaded file where request.POST is give us access to uploaded form field data.
#                                             # we get access file by giving name of that field which we done upper line where in template name='image' which we use here.
#         # store_file(request.FILES['image'])    # Do this when we write code by own self. 
#         # return HttpResponseRedirect('/profiles')

#         submitted_form = ProfileForm(request.POST, request.FILES)   # Handling both if in form data and file are both submitted.
        
#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES['user_image'])
#             profile.save()
#             return HttpResponseRedirect('/profiles')
        
#         return render(request, 'profiles/create_profile.html', {
#             'form': submitted_form
#         })  


# If Not want to use uppper code # Save file
class CreateProfileView(CreateView):
    template_name = 'profiles/create_profile.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/profiles'

# To see all entries at 'profiles/list'
class ProfileView(ListView):
    model = UserProfile
    template_name = 'profiles/user_profile.html'
    context_object_name = 'profiles'