from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'ALL TOOLS',
        'content': 'Главна страница магазина - ALL TOOLS'
    }

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')
