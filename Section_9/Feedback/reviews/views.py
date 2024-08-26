from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review

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