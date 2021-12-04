from django.http.response import FileResponse
from django.shortcuts import get_object_or_404, render

from .models import Image, ImageTag

def home(request):
    return render(request, 'library/home.html')

def image_view(request, id):
    image = get_object_or_404(Image, id=id)
    return FileResponse(open(image.path, "rb"))

def tag_manager(request):
    tags = ImageTag.objects.all().values('name').distinct().order_by('name')
    return render(request, 'library/tag_manager.html', {
        'tags': tags
    })

def by_tag(request, name):
    images = Image.objects.filter(tags__name=name)
    return render(request, 'library/list.html', {
        'images': images
    })
