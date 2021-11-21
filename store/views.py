from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .models import Category, Animal

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_animals(request):
    animals = Animal.objects.all()
    return render(request, 'store/home.html', {'animals': animals})

def animal_detail(request, slug):
    animal = get_object_or_404(Animal, slug=slug, is_active=True)
    return render(request, 'store/animals/detail.html', {'animal': animal})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    animals = Animal.objects.filter(category=category)
    return render(request, 'store/animals/category.html', {'category': category, 'animals': animals})

class CreateAnimal(PermissionRequiredMixin, CreateView):
    template_name = 'store/create_animal.html'
    model = Animal
    success_url = reverse_lazy('store:all_animals')
    fields = '__all__'
    permission_required = 'store.create_animal'

class DeleteAnimal(PermissionRequiredMixin, DeleteView):
    template_name = 'store/delete_animal.html'
    model = Animal
    context_object_name = 'animal'
    success_url = reverse_lazy('store:all_animals')
    permission_required = 'store.delete_animal'

class UpdateAnimal(PermissionRequiredMixin, UpdateView):
    template_name = 'store/update_animal.html'
    model = Animal
    success_url = reverse_lazy('store:all_animals')
    fields = '__all__'
    context_object_name = 'animal'
    permission_required = 'store.change_animal'
