from django.http.response import FileResponse
from django.shortcuts import get_object_or_404, render

from .models import Image, ImageTag

def home(request):
    return render(request, 'library/home.html')

def image_view(request, id):
    image = get_object_or_404(Image, id=id)
    return FileResponse(open(image.path, "rb"))
