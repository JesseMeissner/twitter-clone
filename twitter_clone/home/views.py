from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Photo
from .forms import PostForm, PhotoForm
from cloudinary.forms import cl_init_js_callbacks
 
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.erros.as_json())

    #Get all posts, limit 30
    posts = Post.objects.all()[:30]
    photos = Photo.objects.all()[:30]

    #Display
    return render(request, 'home.html', {'posts': posts, 'photos': photos})


def likePost(request, post_id):
    new_value = Post.objects.get(id=post_id)
    new_value.likes += 1
    new_value.save()
    return HttpResponseRedirect('/')


def loadPhoto(request):
    form = PhotoForm()
    return render(request, 'home.html', {'form': form})


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')