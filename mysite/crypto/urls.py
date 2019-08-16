from django.urls import path
from . import views


app_name = 'crypto'
urlpatterns = [
    path('', views.home, name="home"),
    path('price/', views.prices, name="prices"),
]
