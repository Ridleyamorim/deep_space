from django.shortcuts import render, get_object_or_404
from gallery.models import Photography

def index(request):
    photography = Photography.objects.order_by("date_photography").filter(published=True)

    return render(request, 'gallery/index.html', {"cards": photography})

def imagem(request, photo_id):
    photography = get_object_or_404(Photography, pk=photo_id)

    return render(request, 'gallery/imagem.html', {"photography": photography})
