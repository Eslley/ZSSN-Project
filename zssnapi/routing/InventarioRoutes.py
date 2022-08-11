from django.urls import path
from zssnapi.views import InventarioView

urlpatterns = [
    path('', InventarioView.inventariosList, name='inventarios'),
    path('sobrevivente/<str:fk>/', InventarioView.inventarioDetail, name='inventario-sobrevivente')
]