from django.shortcuts import render, get_object_or_404, redirect
from .models import Cat
from .forms import CatForm

# Create your views here.

def current_cats(request):
  mycats = Cat.objects.all().order_by('age')
  return render(request, 'cat_shelter/current_cats.html', {'mycats' : mycats})

def cat_detail(request, pk):
  cat = get_object_or_404(Cat, pk=pk)
  return render(request, 'cat_shelter/cat_detail.html', {'cat':cat})

def cat_new(request):
  if request.method == "POST":
    form = CatForm(request.POST)
    if form.is_valid():
      cat = form.save()
      return redirect('cat_shelter.views.cat_detail', pk=cat.pk)
  else:
    form = CatForm()
  return render(request, 'cat_shelter/cat_edit.html', {'form': form})

def cat_edit(request, pk):
  cat = get_object_or_404(Cat, pk=pk)
  if request.method == "POST":
    form = CatForm(request.POST, instance=cat)
    if form.is_valid():
      cat = form.save()
      return redirect('cat_shelter.views.cat_detail', pk=cat.pk)
  else:
    form = CatForm(instance=cat)
  return render(request, 'cat_shelter/cat_edit.html', {'form': form})
