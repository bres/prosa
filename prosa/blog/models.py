from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Posts(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft','Draft'),
        ('published','Published'),
               )
    title=models.CharField(max_length=150)
    excerpt=models.TextField(max_length=500,null=True)
    slug =models.SlugField(max_length=250,unique_for_date='publish_date')
    publish_date =models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    content =models.TextField(max_length=5000)
    status=models.CharField(max_length=10,choices=options,default='draft')
    #add in thumbnail
    newmanager=NewManager() # custom manager

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.slug])
    class Meta:
        ordering=('-publish_date',)

    def __str__(self):
        return self.title + ' | ' + str(self.author)


class Comment(models.Model):
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=50)
    email=models.EmailField()
    content=models.TextField(max_length=5000)
    publish=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)


    class Meta:
        ordering=("publish",)

    def __str__(self):
        return f"Comment by {self.name}"
