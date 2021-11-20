from django.shortcuts import render

from .models import Category, Animal

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_animals(request):
    animals = Animal.objects.all()
    return render(request, 'store/home.html', {'animals': animals})
