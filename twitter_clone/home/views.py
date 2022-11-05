from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    #Get all posts, limit 30
    posts = Post.objects.all()[:30]

    #Display
    return render(request, 'home.html', {'posts': posts})