
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns = [
    path('', include('zssnapi.routing.SobreviventeRoutes')),
    path('', include('zssnapi.routing.ItemRoutes')),
    path('', include('zssnapi.routing.InventarioRoutes')),
    path('admin/', admin.site.urls)
]
