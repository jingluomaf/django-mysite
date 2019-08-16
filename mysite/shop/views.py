from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView, View


class HomeView(ListView):
    model = Item
    paginate_by = 10
