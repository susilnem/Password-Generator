from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'home.html')


def result(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 5))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'result.html', {'password': thepassword})

