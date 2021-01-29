from django.shortcuts import render,get_object_or_404,redirect
from .models import Posts
from django.contrib.auth.decorators import login_required
from .forms import CreatePost
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

@login_required(login_url="/accounts/login/")
def post_create(request):
    if request.method=='POST':
        form=CreatePost(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('blog:posts_list')
    else:
        form=CreatePost()
    return render(request,'blog/post_create.html',{'form':form })

def post_edit(request, slug):
    post = get_object_or_404(Posts,slug=slug)
    if request.method == "POST":
        form = CreatePost(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_single', slug=post.slug)
    else:
        form = CreatePost(instance=post)
    return render(request, 'blog/post_update.html', {'form': form,'post':post})
