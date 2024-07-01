from django.urls import path
from . import views
# Here "." means our "urls.py" file inside challenges folder and "views.py" file also inside challenges folder so from "."
# means at the same folder import "views.py" file

urlpatterns = [
    # path("january", views.index),
    # Here path function tack two argument, first argument describes string is "URL" which we want to be supported,
    # second argument is the pointer at the view function that should be executed when the request reaches that url.
    # Here views.index means inside views file "index" name function trigger when january reaches at the url of webpage

    # path("february", views.february),

    # Now for not to write for all month and generate dynamic month

    path("<int:month>", views.monthly_challenge_by_number),  # go:  http://127.0.0.1:8000/challenges/1
    # here int means the routes given by user are integer at the end.

    path("<str:month>", views.monthly_challenges, name="month-challenge"),  # go: http://127.0.0.1:8000/challenges/april
    # here name is keyword argument you can specify whichever you want.
    # Here between written "<?>" (angle bracket) the keyword is for dynamic keyword
    # Note: monthly_challenges is a function which accepts one more argument which same name has written inside angle bracket.

    path("", views.index1)    # /challenges/
]
