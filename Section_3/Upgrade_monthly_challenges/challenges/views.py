from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    months = list(monthly_challenge.keys())
    return render(request, "challenges/index.html", {
        "months": months,
    })


# here we create logic that if number enter by user is 1 then it will redirect to january to archive this functionality:
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenge.keys())

    if month < 1 or month > len(months):
        return HttpResponseNotFound(f"<h1>Invalid month</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])   # /challenge/january
    return HttpResponseRedirect(redirect_path)


# This function for if user directly writes month name as string:
def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
        print(f"Rendering challenge for {month}: {challenge_text}")
        return render(request, "challenges/challenge.html", {"text": challenge_text, "month_name": month})   # this is shortcut method and down is longcut method.
        # Remember:
        # "render" fun. need first argument as "request" and second one is normal html file.
        # The third one is dict. in which key value pair and it pass to template at render time and each key act as vaariable with its value.


        # Basically, here we first fetch the data from a template file and then convert it to string then give user to response.
        # response_data = render_to_string("challenges/challenge.html")
        # here inside template folder another folder same name as app name folder and in upper line we write template file with
        # folder name because if there is so many template file with same name then django is confused so practice to write template name with folder name.
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound(f"<h1>Monthly challenge not found!</h1>")
