from django.shortcuts import render
from .models import Post, Category



# Create your views here.

def home(request):
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    return render(request, 'home.html', {'posts': posts, 'cats': cats})


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request, 'post.html', {'post': post, 'cats': cats})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts= Post.objects.all(cat=cat)
    return render(request, cat.html, {'cat': cat, 'posts': posts})
