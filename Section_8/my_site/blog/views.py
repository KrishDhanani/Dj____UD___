from django.shortcuts import render, get_object_or_404

from .models import Post




# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]     # We fetching only 3 latest post from all posts.
    # Here full line(Post.objects.all().order_by('-date')[:3]) act as sql query so no any 
    # type of performance decreases happen by slicing.
    return render(request, "blog/index.html", {
        "posts": latest_posts,
    })


def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts,
    })


def post_detail(request, slug):  # we should accept slug here bcs in url.py file we use slug as parameter, and we need to catch it when request was happen by user for a particular blog.
    identified_post = get_object_or_404(Post, slug=slug)     # also without using 404 write like: Post.objects.get(slug=slug)
    # Here the next fun. Is used to indicate that post in which user is click and we bypassing inside the fun. That post we can pass that post to post-detail page.
    return render(request, 'blog/post-detail.html', {
        'post': identified_post,
        'post_tags': identified_post.tags.all()    # we need to do this because our tsg is many to many field and we can't use it with (for tag in post.tag)
    })
