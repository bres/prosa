from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('posts/',views.posts_list,name='posts_list'),
    path('create/',views.post_create,name='create'),
    path('<slug:post>/', views.post_single, name='post_single'),
]
 
