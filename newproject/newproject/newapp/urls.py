from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    path('contact/',views.contact,name='contact'),
    path('destinations/',views.destinations,name='destinations'),
    path('elements/',views.elements,name='elements'),
    path('news/',views.news,name='news.html'),
    path('about/',views.about,name='about.html')

]
