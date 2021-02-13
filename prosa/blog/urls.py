from django.urls import path
from . import views

app_name='blog'

urlpatterns = [

    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('posts',views.posts_list,name='posts_list'),
    path('create',views.post_create,name='post_create'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit', views.post_edit, name='post_edit'),
    path('<slug:slug>/delete', views.post_delete, name='post_delete'),

]
