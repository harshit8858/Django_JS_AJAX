from django.shortcuts import render, redirect
from django.http import  JsonResponse, HttpResponse
from .models import *
from django.db.models import Q
from .forms import *


def index(request):
    data = Data.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'js/index.html', context)
    # return JsonResponse('hi', safe=False)


def add(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('')
    else:
        form = TableForm()
    return render(request, 'js/add.html', {'form':form})


def search(request):
    if request.method == 'POST':
        s = request.POST['search']
        if s:
            sa = Data.objects.filter(Q(name__icontains=s)|Q(number__icontains=s))
            if sa:
                return render(request, 'js/search.html', {'data': sa,'t':s})
            else:
                return render(request, 'notfound.html')
        else:
            return redirect('js:index')
