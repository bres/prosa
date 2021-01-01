from django.contrib import admin
from .models  import Posts
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display=('title','status','slug','author')

admin.site.register(Posts,AuthorAdmin)