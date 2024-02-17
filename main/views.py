from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):
    
    categories = Categories.objects.all()

    context = {
        'title': 'Всё для дома',
        'content': 'Интернет-магазин мебели "Всё для дома"',
        'categories': categories
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Всё для дома - О нас',
        'content': 'О нас',
        'text_on_page': 'Описание магазина'
    }
    return render(request, 'main/about.html', context)