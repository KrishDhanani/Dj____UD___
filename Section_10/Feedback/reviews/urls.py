from django.urls import path
from . import views 

urlpatterns = [
    path('', views.ReviewModelView.as_view()),   # because we try to render class based view.
    path('thank-you', views.ThankYouView.as_view()),
    path('reviews', views.ReviewListView.as_view()),
    path('review-detail/<int:pk>', views.ReviewDetailView.as_view(), name='review-detail')  # Here pk means Primary Key
]
