from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='videoIndex'),
    path('detail', views.detail, name='videoDetail'),
    path('live', views.live, name='livePage'),
    path('live-urls', views.live_urls, name='liveUrls')
]
