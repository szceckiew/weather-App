"""
URL configuration for weatherApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, register_converter
from . import views
from .converters import FloatConverter

register_converter(FloatConverter, 'float')

urlpatterns = [
    path('img/<str:filename>/', views.get_img, name='get_img'),
    path('weather/<float:latitude>/<float:longitude>/', views.get_weather_data, name='get_weather_data'),
    path('weather/', views.get_weather_data, name='get_weather_data_no_params'),
    path('', views.index),
]
