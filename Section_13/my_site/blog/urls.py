from django.urls import path
from . import views


urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.AllPostView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page")  # posts/my-first-post
    # instead of use slug you can also use unique id but that was less SEO(Search engine optimization) friendly so use like dash keyword
    # slug transformer(transformer like int, str, slug) basically check the character and in special character only dash(-) allow and if all character match or not
]
