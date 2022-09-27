from multiprocessing import context
from django.shortcuts import render


def home(request):

    return render(request, 'shop_app/index.html', {'title': 'Home'})


def welcome(request):

    return render(request, 'shop_app/welcome.html')
