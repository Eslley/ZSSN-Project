from django.urls import path
from zssnapi.views import ItemView

urlpatterns = [
    path('', ItemView.itensList, name='itens'),
    path('create', ItemView.itemCreate, name='item-create'),

]