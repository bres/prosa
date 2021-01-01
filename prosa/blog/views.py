from django.shortcuts import render
from .models import Posts





# Create your views here.
def home(request):

    return render(request,'blog/home.html')


def posts_list(request):
    posts=Posts.objects.all()
    return render(request,'blog/posts.html',{'posts':posts } )

def about(request):

    return render(request,'blog/about.html')

