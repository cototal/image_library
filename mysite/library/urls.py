from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('', views.home, name='library_home'),
    path('image/<int:id>', views.image_view, name='library_image')
]
