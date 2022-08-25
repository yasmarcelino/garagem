from django.contrib import admin
from django.urls import path,include

from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet, ModelosViewSet, MarcaViewSet, CarroViewSet

router = DefaultRouter()
router.register(r'modelos', ModelosViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'marcas', MarcaViewSet)
router.register(r'carros', CarroViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
]
