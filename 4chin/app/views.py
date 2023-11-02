from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import User, Post, Category, Comment
from datetime import datetime
<<<<<<< Updated upstream
=======
from .serializers import UserSerializer, PostSerializer, CommentSerializer, CategorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

>>>>>>> Stashed changes

def register(request):
    if request.method == 'POST':
        usernameRegister = request.POST['username']
        emailRegister = request.POST['email']
        passwordRegister = request.POST['password']
        user = User(username=usernameRegister, 
                    email=emailRegister, 
                    password=passwordRegister
                    )
        user.save()
        return redirect(f'home/{usernameRegister}')  
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
    context = {
        'username':usernameLogin,
    }
    # CREAR UN POST. DEBERIA SER OTRA VIEW SEPARADA
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

def delete_comment(request, comment_id, username):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('home', usernameLogin=username)
