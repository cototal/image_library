import glob
import os

from ..models import Image

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
