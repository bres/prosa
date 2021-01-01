from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Posts(models.Model):

    options = (
        ('draft','Draft'),
        ('published','Published'),
               )
    title=models.CharField(max_length=150)
    slug =models.SlugField(max_length=250,unique_for_date='publish_date')
    publish_date =models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    content =models.TextField(max_length=2000)
    status=models.CharField(max_length=10,choices=options,default='draft')
    #add in thumbnail
    class Meta:
        ordering=('-publish_date',)

    def __str__(self):
        return self.title + ' | ' + str(self.author)