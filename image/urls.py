from django.urls import path

from image import views

urlpatterns = [

    path('', views.Home, name='home'),
    path('portfolio', views.Portfolio, name='portfolio'),
    path('elements', views.Elements, name='elements'),


]
