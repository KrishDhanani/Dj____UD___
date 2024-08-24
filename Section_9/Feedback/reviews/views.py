from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def review(request):

    if request.method == 'POST':        # Here we check wether submitted form is submit by POST metod or not.
        entered_username = request.POST['username']     
        # Here request means read some data from request
        # Then POST is method through which data was submitted and it hold dictionary of data. 
        # Here name is act as dictionary's key and by which we gwt data 
        print(entered_username)
        # return render(request, 'reviews/thankyou.html')
        # we can't(could but not recomanded) render template bcs POST method use to post data to the server so we use another function here.
        if entered_username == '' or len(entered_username)>100: # Manually validation check
            return render(request, 'reviews/review.html', {
                'has_error': True
            })
        return HttpResponseRedirect('/thank-you')
    
    return render(request, 'reviews/review.html', {
        'has_error': False
    })

def thank_you(request):
    return render(request, 'reviews/thank_you.html')