from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .forms import UserRegisterForm, UserLoginForm, PostForm
from .models import Post, Category

def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'page_obj':page_obj, 'request':request})


def get_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/singlepost.html', {'post':post})

def get_category(request, slug):
    posts = Post.objects.filter(category__slug=slug)
    category_post = Post.objects.filter(category__slug=slug)[0]
    return render(request, 'blog/categoryposts.html', {'posts': posts, 'category_post' : category_post})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегестрировались")
            return redirect("login")
        else:
            messages.error(request, "Ошибка регистрации")

    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {"form" : form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'blog/login.html', {'form' : form})

def user_logout(request):
    logout(request)
    return redirect('login')

def get_profile(request, username):
    posts = Post.objects.filter(author=username)
    return render(request, 'blog/profile.html', {'posts' : posts})

# def add_news(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             news = Post.objects.create(**form.cleaned_data)
#             return redirect('home')
#             # news = form.save()
#             # return redirect(news)
#     else:
#         form = PostForm()
#     return render(request, 'blog/add_post.html', {"form" : form})


@login_required()
def CreatePost(request):
    categories = Category.objects.all()
    if User.is_authenticated:
        if request.method == "POST":

            form = PostForm(request.POST)
            if form.is_valid():
                form.save(commit=False)
                form.save()
                return redirect('home')
        else:
            form = PostForm()
        author = request.user.username
        return render(request, 'blog/add_post.html', {"form": form, "author" : author, "categories":categories})

# def posts_by_month(request):
#     pass

