from django.urls import path
from zssnapi.views import ComercioView

urlpatterns = [
    path('', ComercioView.negociar, name='negociar'),

]