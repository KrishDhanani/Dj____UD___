from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm, ReviewModelForm
from .models import Review
from django.views import View

# Create your views here.

def review(request):

    if request.method == 'POST':        # Here we check wether submitted form is submit by POST metod or not.
        # entered_username = request.POST['username']     
        # Here request means read some data from request
        # Then POST is method through which data was submitted and it hold dictionary of data. 
        # Here name is act as dictionary's key and by which we gwt data 
        # print(entered_username)
        # return render(request, 'reviews/thankyou.html')
        # we can't(could but not recomanded) render template bcs POST method use to post data to the server so we use another function here.
        # if entered_username == '' or len(entered_username)>100: # Manually validation check
        #     return render(request, 'reviews/review.html', {
        #         'has_error': True
        #     })
        # return HttpResponseRedirect('/thank-you')

        form = ReviewForm(request.POST)

        if form.is_valid():           # Check wether form was submitted currectly.
            review = Review(user_name=form.cleaned_data['user_name'], 
                            review_text=form.cleaned_data['review_text'], 
                            rating=form.cleaned_data['rating'])
            review.save()       # Saving Data to Database
            print(form.cleaned_data)    # Here cleaned_data holds data in dictionary form which is submitted at form type.
            return HttpResponseRedirect("/thank-you")        
            
    else:
        form = ReviewForm()
        return render(request, 'reviews/review.html', {
            "form": form, 
        # 'has_error': False
        })  

def thank_you(request):
    return render(request, 'reviews/thank_you.html')


# Class Based View using
# model form
class ReviewModelView(View):        # Inheriting class From Django View
    def get(self, request):
        mform = ReviewModelForm()
        return render(request, 'reviews/review.html', {
            "mform": mform
            })

    def post(self, request):
        mform = ReviewModelForm(request.POST)
        if mform.is_valid():
            mform.save()        # as ago we no need to write code or assign value to model  which is fetch form submission. because of this form is model form we simply save the data to the database.  
            return HttpResponseRedirect('/thank-you')