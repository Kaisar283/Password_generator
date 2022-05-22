from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghigklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIGKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()_+{}[]?'))

    if request.GET.get('number'):
        characters.extend(list('1234567890'))

    lengh = int(request.GET.get('length', 12))
    thepassword = ""

    for i in range(lengh):
        thepassword += random.choice(characters)


    return render(
        request,  # request
        'generator/password.html',  # template_name
        {'password': thepassword}  # context
    )

def discription(request):
    return render(request, 'generator/discription.html')
