from .models import User, Post, Category, Comment

def my_context_processor(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    comments = Comment.objects.all()
    name = "4chin"

    context = {
        'siteName': name,
        'posts': posts,
        'categories': categories,
        'comments': comments,
        'status': True
    }
    return context