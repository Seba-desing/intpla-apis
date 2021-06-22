from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('boleta', BoletaViewset)
router.register('despacho', DespachoViewset)
router.register('marca', MarcaViewset)
router.register('stock', StockViewset)

urlpatterns = [    
    path('api/', include(router.urls)),
]
