from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.erros.as_json())

    #Get all posts, limit 30
    posts = Post.objects.all()[:30]

    #Display
    return render(request, 'home.html', {'posts': posts})