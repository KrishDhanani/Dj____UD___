from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewModelForm
from django.views.generic.base import TemplateView
from .models import ReviewModel
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView  # It automaticaly save data to model on form submission which can not done by form view

# Create your views here.

# Class Based View using
# model form
class ReviewModelView(FormView):    
    form_class = ReviewModelForm
    template_name = 'reviews/review.html'
    # since we using FormView to see form fields need to 'form' variable in template file. 

    success_url = '/thank-you'   # It is for If form is submitted without generating any error then where to redirect.

    # To save data in database
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

    # Here when we use FormView no need to specify get method it automatically handle by Django.
    # def get(self, request):
    #     mform = ReviewModelForm()
    #     return render(request, 'reviews/review.html', {
    #         "mform": mform
    #         })

    # def post(self, request):
    #     mform = ReviewModelForm(request.POST)
    #     if mform.is_valid():
    #         mform.save()       
    #         return HttpResponseRedirect('/thank-you')


# class ThankYouView(View):
#     def get(self, request):
#         return render(request, 'reviews/thank_you.html')


class ReviewModelView(CreateView):    
    model = ReviewModel     # We need to specify on which model data save
    form_class = ReviewModelForm 
    template_name = 'reviews/review.html'
    # since we using FormView to see form fields need to 'form' variable in template file. 

    success_url = '/thank-you'   # It is for If form is submitted without generating any error then where to redirect.
    

class ThankYouView(TemplateView):   # Insted of simple view inheriting we inheriting here TemplateView
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):       # To pass data in template(thank_you.html)
        context = super().get_context_data(**kwargs)    # need to called from TemplateView and call it   # This line means get the context from parent class
        context['message'] = 'Thank You!'
        # Inside [] written is variable and to see how it is used goto thank_you.html 
        return context
    
class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = ReviewModel
    # Django will directly pass all reviews to review_list.html and the name of variable is 'object_list' but we can change like;
    context_object_name = 'reviews' 

    # If we want to pass only those review which has rating greater than 4 then;
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data   
    
class ReviewDetailView(DetailView):
    template_name = 'reviews/review_detail.html'
    model = ReviewModel
    # How Django find a perticuler data is based on 'slug' or 'primary key'. Here we done it by using primarykey so in url need to specify 'pk'.
    # If we done using slug then need to specify in url 'slug'.
    # Remember: In template file you can use variable name as in lowercase 'model name' or 'object' which we here specify in review_detail.html 

    # J.J. if insted of DetailView we use TemplateView then what to write; 
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs['pk']
    #     review = ReviewModel.objects.get(id=review_id)
    #     context['review'] = review
    #     return context

