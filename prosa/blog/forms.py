from django import forms

from .models import Posts,Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ('title', 'slug','content','excerpt','status')



class NewCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email','content')
