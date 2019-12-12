from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/auth/login/')
def manage(request):
    return render(request, 'manage.html')
