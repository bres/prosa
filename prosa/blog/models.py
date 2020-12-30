from django.db import models

# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=150)
    slug =models.SlugField()
    body =models.TextField(max_length=2000)
    date =models.DateTimeField(auto_now_add=True)
    #add in thumbnail
    #add author

    def __str__(self):
        return self.title