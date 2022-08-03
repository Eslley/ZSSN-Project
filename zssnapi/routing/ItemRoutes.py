from django.urls import path
from zssnapi.views import ItemList

urlpatterns = [
    path('itens/', ItemList.as_view()),

]