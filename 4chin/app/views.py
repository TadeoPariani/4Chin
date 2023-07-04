from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .models import User, Post, Category, Comment
from datetime import datetime

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User(username=username, 
                    email=email, 
                    password=password
                    )
        user.save()
        return redirect('home')  
    return render(request, 'app/register.html')


def login(request):
    try:
        usernameLogin = request.POST['username']
        passwordLogin = request.POST['password']
        user = User.objects.get(username=usernameLogin)
        if passwordLogin == user.password:
            return redirect(f'home/{usernameLogin}')
    except:
        Status =  False
        context = {
            "Status": Status
        }
        return render(request, 'app/login.html', context)
    return render(request, 'app/login.html')


def home(request, usernameLogin):
    users = User.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.all()
    comments = Comment.objects.all()
    
    context = {
        'users': users,
        'username':usernameLogin,
        'categories':categories,
        'posts':posts,
        'comments': comments
    }

    if request.method == "POST":
        author = User.objects.get(username=usernameLogin)
        creation_date = datetime.now()
        title = request.POST['title']
        content = request.POST['content']
        category_id = request.POST['category']
        category = Category.objects.get(id=category_id)
        newPost = Post(
            title=title,
            creation_date=creation_date, 
            author=author, 
            content=content, 
            category=category
            )
        newPost.save()
        return render(request, 'app/home.html', context)
    return render(request, 'app/home.html', context)

def delete_post(request, post_id, username):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('home', usernameLogin=username)

def make_comment(request, post_id, username):
    author = User.objects.get(username=username)
    post = Post.objects.get(id=post_id)
    comment = request.POST['comment']
    creation_date = datetime.now()
    newComment = Comment(text=comment, author=author, post=post, creation_date = creation_date )
    newComment.save()
    return redirect('home', usernameLogin=username)