from django.urls import path
from . import views

# 'urlpatterns' <= same write 
urlpatterns = [
    path('meetups/', views.index)    # our_domain.com/meetups/  # always add '/' after name is good practice.
]
