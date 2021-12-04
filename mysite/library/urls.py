from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('', views.home, name='home'),
    path('tags', views.tag_manager, name='tags'),
    path('tags/<name>', views.by_tag, name='by_tag'),
    path('image/<int:id>', views.image_view, name='image')
]
