from django.shortcuts import render, get_object_or_404
from .models import Cat

# Create your views here.

def current_cats(request):
  mycats = Cat.objects.all().order_by('age')
  return render(request, 'cat_shelter/current_cats.html', {'mycats' : mycats})

def cat_detail(request, pk):
  cat = get_object_or_404(Cat, pk=pk)
  return render(request, 'cat_shelter/cat_detail.html', {'cat':cat})
