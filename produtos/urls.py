from . import views
from django.urls import path
from produtos.views import ProductListView, ProductDetailView

app_name = 'produtos'


urlpatterns = [
    path('', ProductListView.as_view(), name='listagem'),
    path('detalhes-produto/<int:id>', ProductDetailView.as_view(), name='detalhes'),
]
