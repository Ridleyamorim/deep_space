from django.urls import path
from gallery.views import imagem, index, buscar

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:photo_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar')
]
