from django.shortcuts import render, redirect
from .models import Client
from .models import BonusCard
from .forms import ClientForm
from .forms import BonusCardForm
from django.views.generic import DetailView, UpdateView, DeleteView

class ClientDeleteView(DeleteView):
    model = Client
    success_url = '/bonus/'
    template_name = 'bonus/delete.html'

class CardDeleteView(DeleteView):
    model = BonusCard
    success_url = '/bonus/'
    template_name = 'bonus/delete.html'

class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'bonus/create.html'
    form_class = ClientForm

class CardUpdateView(UpdateView):
    model = BonusCard
    template_name = 'bonus/create_card.html'
    form_class = BonusCardForm


class ClientDetailView(DetailView):
    model = Client
    template_name = 'bonus/details_view_client.html'
    context_object_name = 'client'

class CardDetailView(DetailView):
    model = BonusCard
    template_name = 'bonus/details_view_card.html'
    context_object_name = 'card'

def bonus_home(request):
    cards = BonusCard.objects.all()
    return render(request, 'bonus/bonus_home.html', {'cards': cards})

def client_home(request):
    clients = Client.objects.order_by('surname')[:10]
    return render(request, 'bonus/client_home.html', {'clients': clients})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Некорректные данные'

    form = ClientForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'bonus/create.html', data)


def create_card(request):
    error = ''
    if request.method == 'POST':
        form = BonusCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Некорректные данные'

    form = BonusCardForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'bonus/create_card.html', data)

