from . import views
from django.urls import path
from produtos.views import ProductListView


urlpatterns = [
    path('', ProductListView.as_view(), name='produtos'),
]
