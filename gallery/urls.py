from django.urls import path
from gallery.views import imagem, index

urlpatterns = [
    path('', index, name='index'),
    path('imagem.html', imagem, name='imagem') 
]
