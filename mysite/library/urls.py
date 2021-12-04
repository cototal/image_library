from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('', views.home, name='home'),
    path('tags', views.tag_manager, name='tags'),
    path('tags/add-remove', views.add_remove_tags, name='tags_add_remove'),
    path('tags/<name>', views.by_tag, name='by_tag'),
    path('image/<int:id>', views.image_view, name='image'),
    path('tag-list', views.tag_list, name='tag_list')
]
