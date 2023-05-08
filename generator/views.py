from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def description(request):
    return render(request, 'generator/description.html')


def password(request):
    const_len1 = 12
    const_len2 = 40

    character = list(chr(i) for i in range(97, 123))
    try:
        length = int(request.GET.get('length'))
    except:
        length = const_len1
    if request.GET.get('uppercase'):
        character.extend(list(chr(i) for i in range(65, 91)))
    if request.GET.get('numbers'):
        character.extend(list(str(i) for i in range(0, 10)))
    if request.GET.get('special'):
        character.extend(list(chr(i) for i in range(33, 48)))

    thepassword = ''
    if length > 40:
        length = const_len2
    for elem in range(length):
        thepassword += random.choice(character)

    return render(request, 'generator/password.html', {'password': thepassword})
