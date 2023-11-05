from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from produtos.models import Products


class ProductListView(ListView):
    model = Products
    context_object_name = 'produtos'
    template_name = 'produtos/product_list.html'


class ProductDetailView(DetailView):
    model = Products
    context_object_name = 'produto'
    template_name = 'produtos/detalhar.html'
    pk_url_kwarg = 'id'
