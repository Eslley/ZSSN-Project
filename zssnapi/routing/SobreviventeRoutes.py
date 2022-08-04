from django.urls import path
from zssnapi.views import SobreviventeView

urlpatterns = [
    path('', SobreviventeView.sobreviventesList, name='sobreviventes'),
    path('detail/<str:pk>/', SobreviventeView.sobreviventeDetail, name='sobrevivente-detail'),
    path('create', SobreviventeView.sobreviventeCreate, name='sobrevivente-create'),
    path('update/<str:pk>/', SobreviventeView.sobreviventeUpdate, name='sobrevivente-update'),
    path('update/<str:pk>/localization/', SobreviventeView.sobreviventeUpdateLocalization, name='sobrevivente-update-localization'),
    path('delete/<str:pk>/', SobreviventeView.sobreviventeDelete, name='sobrevivente-delete'),

]