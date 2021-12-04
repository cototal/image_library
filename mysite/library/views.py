import json

from django.http.response import FileResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST

from .models import Image, ImageTag
from .utils import string_utils

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
    images = Image.objects.filter(tags__name=name).distinct()
    return render(request, 'library/list.html', {
        'images': images
    })

def tag_list(request):
    tags = ImageTag.objects.all().values('name').distinct().order_by('name')
    tag_names = [t['name'] for t in tags]
    return JsonResponse({'names': tag_names})

@require_POST
def add_remove_tags(request):
    json_data = json.loads(request.body)
    for image_id in json_data['ids']:
        image = Image.objects.get(id=image_id)
        image_tag = None
        try:
            image_tag = ImageTag.objects.get(image=image, name=json_data['name'])
        except ImageTag.DoesNotExist:
            pass
        except ImageTag.MultipleObjectsReturned:
            image_tag = ImageTag.objects.filter(image=image, name=json_data['name'])[:1].get()

        if json_data['action'] == 'remove' and image_tag is not None:
            image_tag.delete()
        elif json_data['action'] == 'add' and image_tag is None:
            image_tag = ImageTag(image=image, name=string_utils.parameterize(json_data['name']))
            image_tag.save()

    return JsonResponse(json_data)
