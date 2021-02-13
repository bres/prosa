from django.shortcuts import render,get_object_or_404,redirect
from .models import Posts
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'blog/home.html')

def posts_list(request):
    posts=Posts.newmanager.all()
    return render(request,'blog/posts.html',{'posts':posts } )

def about(request):
    return render(request,'blog/about.html')

def post_detail(request,slug):
    post=get_object_or_404(Posts,slug=slug,status='published')
    return render(request,'blog/post_detail.html',{'post':post})


@login_required(login_url="/accounts/login/")
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:posts_list')
    else:
        form = PostForm()
    context={
                'form':form
            }
    return render(request,'blog/post_create.html', context)

@login_required(login_url="/accounts/login/")
def post_edit(request, slug):
    post = get_object_or_404(Posts, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail',slug=post.slug)
    else:
        form = PostForm(instance=post)
        context={
            'form':form
        }
    return render(request, 'blog/post_edit.html', context)




@login_required(login_url="/accounts/login/")
def post_delete(request, slug):
    post = get_object_or_404(Posts, slug=slug)
    if post.author != request.user:
        return redirect('blog:posts_list')
    if request.method == 'POST':
        post.delete()
        return redirect('blog:posts_list')

    context ={
        'post':post
    }

    return render(request, 'blog/post_confirm_delete.html',context)
