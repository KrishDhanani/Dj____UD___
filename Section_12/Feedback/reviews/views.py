from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewModelForm
from django.views.generic.base import TemplateView
from .models import ReviewModel
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView  
from django.views import View

# Create your views here.

# Class Based View using
# model form
class ReviewModelView(FormView):    
    form_class = ReviewModelForm
    template_name = 'reviews/review.html'

    success_url = '/thank-you'   

    # To save data in database
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ReviewModelView(CreateView):    
    model = ReviewModel     
    form_class = ReviewModelForm 
    template_name = 'reviews/review.html'

    success_url = '/thank-you'   
    

class ThankYouView(TemplateView):   
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):       
        context = super().get_context_data(**kwargs)    
        context['message'] = 'Thank You!'
        return context
    
class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = ReviewModel
  
    context_object_name = 'reviews' 

    
class ReviewDetailView(DetailView):     # Modified
    template_name = 'reviews/review_detail.html'
    model = ReviewModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object         # object: It give us that review detail which is automatically loaded
        request = self.request
        favorite_id = request.session.get("favorite_review")        # 'favorite_review' this key in dic of session
        context['is_favorite'] = favorite_id == str(loaded_review.id)   # we convert in str bcs everithing submited by form is str form
        return context
   

# New Added
class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        # fav_review = ReviewModel.objects.get(pk=review_id)  # Finding review in database
        # bcs of upper line generate error at storing in session bcs it return Object which Django can't store in Session.  

        # Storing in Session
        request.session["favorite_review"] = review_id     # Adding new session with 'favorite_review' key.
        return HttpResponseRedirect("/review-detail/" + review_id)