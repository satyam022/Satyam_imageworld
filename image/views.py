from django.shortcuts import render
from .models import World


# Create your views here.

def Home(request):
    return render(request, 'index.html')


def Elements(request):
    return render(request, 'elements.html')


def Portfolio(request):
    data = World.objects.all()

    context = {
        'data': data
    }

    return render(request, 'portfolio.html', context)
