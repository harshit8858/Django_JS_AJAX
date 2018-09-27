from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q


def index(request):
    data = Data.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'js/index.html', context)


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