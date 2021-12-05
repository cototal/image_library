from django import template
from django.conf import settings
from django.templatetags.static import static

register = template.Library()

@register.filter()
def thumbnail_path(image):
    img_exts = ['png', 'jpg', 'jpeg', 'bmp', 'webp']
    ext = image.path.split('.')[-1]
    if ext.lower() in img_exts:
        return static(f'thumbnails/{image.id}.webp')
    return static(f'thumbnails/{image.id}.{ext}')
