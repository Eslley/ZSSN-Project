from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('sobreviventes/', include('zssnapi.routing.SobreviventeRoutes')),
    path('itens/', include('zssnapi.routing.ItemRoutes')),
    path('inventarios/', include('zssnapi.routing.InventarioRoutes')),
    path('comercio/', include('zssnapi.routing.ComercioRoutes')),
    path('admin/', admin.site.urls)
]
