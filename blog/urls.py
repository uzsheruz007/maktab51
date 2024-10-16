from django.urls import path
from . import views
from .views import index,  about, services,  contact, blog

urlpatterns = [

    path('', index, name='index'),
    path('about/', about, name='about'),
   
    path('services/',  services, name='services'),
    path('contact/',  contact,  name='contact'),
    path('blog/',  blog, name='blog')
  
]

