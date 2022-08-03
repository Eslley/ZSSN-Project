from django.urls import path
from zssnapi.views import InventarioList

urlpatterns = [
    path('inventarios/', InventarioList.as_view()),

]