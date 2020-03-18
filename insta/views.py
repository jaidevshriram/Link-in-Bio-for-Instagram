from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User 
from .models import *
from .forms import NewPost

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/create-post')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print(request.POST)
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'insta/login.html')

def index(request):
    posts = Post.objects.all()
    return render(request, 'insta/index.html', { 'posts': posts })

@login_required
def create_post(request):
    if request.method == 'POST':
        form = NewPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
            return HttpResponse("Post couldn't be created")
    else:
        form = NewPost()
    return render(request, 'insta/create-post.html')