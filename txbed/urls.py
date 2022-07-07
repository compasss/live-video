from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='txbedIndex'),
    path('upload', views.upload, name='fileUpload')
]
