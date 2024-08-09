from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from .views import GetFromUrl, GetAll, GetById, UpdateId, DeleteId, CreateData

app = 'parse'

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('getFromApi', GetFromUrl.as_view()),
    path('GetAll', GetAll.as_view()),
    path('GetById/<int:pk>/', GetById.as_view()),
    path('CreateData', CreateData.as_view()),
    path('UpdateId/<int:pk>/', UpdateId.as_view()),
    path('DeleteId/<int:pk>/', DeleteId.as_view()),
]
