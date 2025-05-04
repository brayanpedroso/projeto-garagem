from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

# Importando a view que você já criou
from core.views import UserViewSet

# Configuração do roteador para a API de usuários
router = DefaultRouter()
router.register(r'usuarios', UserViewSet, basename='usuarios')

urlpatterns = [
    # Rota do Admin do Django
    path('admin/', admin.site.urls),
    
    # OpenAPI 3 para a documentação da API
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    
    # API do Core (Usuarios)
    path('api/', include(router.urls)),  # Inclui as rotas do core.urls
]
