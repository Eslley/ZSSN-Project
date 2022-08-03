from django.urls import path
from zssnapi.views import SobreviventeList

urlpatterns = [
    path('sobreviventes/', SobreviventeList.as_view(), name='sobrevivente-list'),

]