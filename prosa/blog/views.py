from django.shortcuts import render
from .models import Posts





# Create your views here.
def home(request):

    return render(request,'blog/home.html')


def articles_list(request):
    articles=Posts.objects.all().order_by('date')
    return render(request,'blog/articles.html',{'articles':articles } )

def about(request):

    return render(request,'blog/about.html')

