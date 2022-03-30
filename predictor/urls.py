from django.urls import path
from . import views

urlpatterns = [
    path('heart', views.heart, name="heart"),
     path('', views.index, name="imdex"),
    path('diabetes', views.diabetes, name="diabetes"),
    path('breast', views.breast, name="breast"),
    path('', views.home, name="home"),
]

