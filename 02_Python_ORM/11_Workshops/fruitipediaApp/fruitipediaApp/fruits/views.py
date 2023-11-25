from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from fruitipediaApp.fruits.models import Fruit
from fruitipediaApp.fruits.forms import CategoryCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits,
    }
    return render(request, 'common/dashboard.html', context)


# Using Class Base View
# Should import FormView (from django.views.generic import FormView)
# in app urls should use:
# path('create_fruit/', views.FruitFormView.as_view(), name='Fruit creation')
class FruitFormView(FormView):
    form_class = FruitCreateForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)


def details_fruit(request, fruit_pk):
    fruit = Fruit.objects.filter(pk=fruit_pk).get()

    context = {
        'fruit': fruit,
    }
    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request, fruit_pk):
    fruit = Fruit.objects.filter(pk=fruit_pk).get()

    if request.method == 'POST':
        form = FruitEditForm(request.POST, instance=fruit)

        if form.is_valid():
            form.save()

            return redirect('dashboard')

    else:
        form = FruitEditForm(instance=fruit)

    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruits/edit-fruit.html', context)


def delete_fruit(request, fruit_pk):
    fruit = Fruit.objects.filter(pk=fruit_pk).get()

    if request.method == 'POST':
        form = FruitDeleteForm(request.POST, instance=fruit)

        if form.is_valid():
            fruit.delete()

            return redirect('dashboard')

    else:
        form = FruitDeleteForm(instance=fruit)

    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruits/delete-fruit.html', context)


def create_category(request):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('dashboard')

    else:
        form = CategoryCreateForm()

    context = {
        'form': form,
    }
    return render(request, 'categories/create-category.html', context)
