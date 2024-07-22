from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# "reverse" super important function

# Create your views here.
# For seeing output comment dynamic
# def index(request):
#     return HttpResponse("This Works!")
#
#
# def february(request):
#     return HttpResponse("Walk for 20 min every day!")

monthly_challenge = {
    "january": "This Challenge is January!",
    "february": "This Challenge is February!",
    "march": "This Challenge is March!",
    "april": "This Challenge is April!",
    "may": "This Challenge is May!",
    "june": "This Challenge is June!",
    "july": "This Challenge is July!",
    "august": "This Challenge is August!",
    "september": "This Challenge is September!",
    "october": "This Challenge is October!",
    "november": "This Challenge is November!",
    "december": "This Challenge is December!",
}


def index1(request):
    list_items = ""
    months = list(monthly_challenge.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li><br>"

    # "<li><a href="...">january</a></li><li><a href="...">february</a></li>..."
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


# here we create logic that if number enter by user is 1,then it will redirect to january to archive this functionality:
# /challenges/1   -->(Transfer to string function) /challenges/january
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenge.keys())   # keys() function return list object which has all the keys which inside the dictionary and
    # remember keys in Python dictionaries are automatically ordered alphabetically in Python 3.9 and above.

    if month < 1 or month > len(months):
        return HttpResponseNotFound(f"<h1>Invalid month</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])   # /challenge/january
    # reverse fun. allows us to create paths by referring name of this path of these urls
    # first part of fun. indicate referring name and second part is our number of dynamic segments, and here we have only one dynamic segment
    return HttpResponseRedirect(redirect_path)

    # return HttpResponseRedirect("/challenges/" + redirect_month)   # this line is for hardcoded url and the upper part is dynamically generated form.
    # "HttpResponseRedirect" to redirect our existing url to specific some of the url


# This function for if user directly writes month name as string:
def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound(f"<h1>Monthly challenge not found!</h1>")
