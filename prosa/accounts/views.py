from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout
# Create your views here.

def signup_view(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			#log the user in
			return redirect('blog:posts_list')
	else:
		form=UserCreationForm()
	return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log user
            user =form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('blog:home')

    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form })

def logout_view(request):
	if request.method=='POST':
		logout(request)
		return redirect('blog:posts_list')
 
