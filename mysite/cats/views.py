from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Breed, Cat

class BreedList(LoginRequiredMixin, View):
    def get(self, request):
        bl = Breed.objects.all()
        ctx = {'breed_list': bl}
        return render(request,'breed/breed_list.html', ctx)

class BreedCreate(CreateView, LoginRequiredMixin):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')



##Cat View
class CatList(LoginRequiredMixin, View):
    def get(self, request):
        bc = Breed.objects.all().count()
        cl = Cat.objects.all()
        ctx = {'breed_count': bc, 'cats_list': cl}
        return render(request,'cats/cats_list.html', ctx)

class CatCreate(CreateView, LoginRequiredMixin):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')