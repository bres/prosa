from django.shortcuts import render,get_object_or_404
from .models import Posts


# Create your views here.
def home(request):

    return render(request,'blog/home.html')


def posts_list(request):
    posts=Posts.newmanager.all()
    return render(request,'blog/posts.html',{'posts':posts } )

def about(request):

    return render(request,'blog/about.html')

def post_single(request,post):
    post=get_object_or_404(Posts,slug=post,status='published')
    return render(request,'blog/single.html',{'post':post})