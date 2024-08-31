from typing import Any
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Post
from django.views.generic import ListView
from .forms import CommentForm
from django.views import View
from django.http import HttpResponseRedirect


# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = 'posts'

    def get_queryset(self):
        queryset =  super().get_queryset()
        data = queryset[:3]
        return data

class AllPostView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ["-date"]
    context_object_name = 'all_posts'


class SinglePostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request, 'blog/post-detail.html', context)

    def post(self, request, slug): 
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)   # take user input
            comment.post = post    # Add Extra Data
            comment.save()  # save that edited data to database
            # what we done upper side is we exclude in commentform rendring 'post' name field; when we render again that page then need 
            # to ensure that currect post is render. So before save here we do some changes.  
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request, 'blog/post-detail.html', context)
