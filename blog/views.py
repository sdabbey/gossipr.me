from django.shortcuts import render,redirect
from random_username.generate import generate_username

from .models import Post
def home(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, "blog/index.html", {'posts': posts})

def create_post(request):
    
    if request.method == "POST":
        username = generate_username(1)[0]
        content = request.POST.get("content")
        image = request.POST.get("image")
        post = Post.objects.create(username=username, content=content, image=image)
    return redirect('/')



