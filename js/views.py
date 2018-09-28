from django.shortcuts import render, redirect
from django.http import  JsonResponse, HttpResponse
from .models import *
from django.db.models import Q
from .forms import *
from django.template.loader import render_to_string
from django.core import serializers
import json


def index(request):
    data = Data.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'js/index.html', context)
    # return JsonResponse('hi', safe=False)


def add(request):
    data = Data.objects.all()
    data_json =serializers.serialize('json',data)
    data_dumps = json.dumps(data_json)
    # print('data')
    # print(data)
    # print('data_json')
    # print(data_json)
    # print('data_dumps')
    # print(data_dumps)
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            # if request.is_ajax():
            #     print("hi")
            #     html = render_to_string('js/add.html', {'form':form}, request=request)
            #     return JsonResponse({'form':html})
            # html = render_to_string('js/add.html', {'form': form}, request=request)
            # return JsonResponse({'form':html})
            # return JsonResponse(data_json,safe=False)
            return HttpResponse(data_json, content_type="application/json")
            # return JsonResponse('hi',safe=False)
            # return redirect('js:add')

    else:
        form = TableForm()
    return render(request, 'js/add.html', {'form':form, 'data':data})


def search(request):
    if request.method == 'POST':
        s = request.POST['search']
        # if s:
        sa = Data.objects.filter(Q(name__icontains=s)|Q(number__icontains=s))
            # if sa:
            #     return render(request, 'js/search.html', {'data': sa,'t':s})
            # else:
            #     return render(request, 'notfound.html')
        return render(request, 'js/search.html', {'data': sa, 't': s})
        # else:
        #     return redirect('js:index')
