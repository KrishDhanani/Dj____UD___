from django.urls import path
from . import views 

urlpatterns = [
    #path('', views.review),
    path('', views.ReviewModelView.as_view()),   # because we try to render class based view.
    path('thank-you', views.thank_you)
]
