from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/auth/login/')
def manage(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = DocumentForm

    return render(request, 'manage.html', {'form': form})
