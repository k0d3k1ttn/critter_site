from django.shortcuts import render
from .models import Cat

# Create your views here.

def current_cats(request):
  mycats = Cat.objects.all().order_by('age')
  return render(request, 'cat_shelter/current_cats.html', {'mycats' : mycats})
