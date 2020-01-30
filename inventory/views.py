from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
    holidays = DiasLibre.objects.all()
    return render(request, "index.html", {"holidays": holidays})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def menu(request):
    menuCategories = CategoriasDelMenu.objects.all()
    menu_dictionary = dict()
  
    for category in menuCategories:
        menuItems: MenuItem.objects.filter( category=F( category.name))
        menu_dictionary[category.name] = list(menuItems)
        
    return render( request, "menu.html", {"menu_dictionary": menu_dictionary})
