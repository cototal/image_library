from django.db import models

class Image(models.Model):
    path = models.CharField(max_length=2000, db_index=True)
    category = models.CharField(max_length=250, db_index=True)

class ImageTag(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=250, db_index=True)
