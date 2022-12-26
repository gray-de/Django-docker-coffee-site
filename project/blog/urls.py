from django.contrib import admin
from django.urls import path, include
from .views import index, get_post, get_category, register, user_login, get_profile, user_logout, CreatePost

urlpatterns = [
    path('', index, name='home'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('post/<str:slug>/', get_post, name='post'),
    path('category/<str:slug>/', get_category, name='category'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('profile/<str:username>', get_profile, name='profile'),
    path('logout/', user_logout, name='logout'),
    path('add-post/', CreatePost, name='add-post'),
    path('accounts/login/', user_login),
]