import glob
import os

from ..models import Image, ImageTag
from ..utils import string_utils

# from library.scripts import load_image_dir
# load_image_dir.get_all(".")
def get_all(base_dir):
    files = glob.glob(os.path.join(base_dir, "**", "*.*"), recursive=True)
    img_exts = ['png', 'jpg', 'gif', 'svg', 'jpeg', 'bmp', 'webp']
    for file in files:
        ext = file.split('.')[-1]
        if ext.lower() not in img_exts:
            continue

        try:
            image = Image.objects.get(path=file)
        except Image.DoesNotExist:
            image = Image(path=file)
            image.save()
            tag_all([image])

# from library.scripts import load_image_dir
# from library.models import Image, ImageTag
# images = Image.objects.all()
# load_image_dir.tag_all(images)
def tag_all(images, separator='\\', ignore=[]):
    ignored = ignore + ['c:', 'users', 'downloads', 'l:', 'new folder']
    for image in images:
        tags = ImageTag.objects.filter(image=image)
        tag_names = [t.name for t in tags]
        path_parts = image.path.split(separator)[:-1]
        for part in path_parts:
            part = string_utils.parameterize(part)
            if part not in tag_names and part not in ignored:
                image_tag = ImageTag(image=image, name=part)
                image_tag.save()

def parameterize_all(tags):
    for tag in tags:
        tag.name = string_utils.parameterize(tag.name)
        tag.save()
