from django.urls import path,include
from .views import post_content

urlpatterns = [ 
    path('post_content', post_content) 
]