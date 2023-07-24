

from django.urls import path
from . import views
from .img_search import img


from .video_search import video

urlpatterns = [
    path('',views.searchs),
    path('images' ,img),
    path('videos',video)
    
]
