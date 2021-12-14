from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic
from blog.models import Post


# Create your views here.
def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})

def post_detail(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": post})