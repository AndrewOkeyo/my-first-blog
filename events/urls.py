from django.urls import path
from . import views


urlpatterns = [
    path('', views.firstpage, name="firstpage"),
    path('events/', views.index, name="index"),
    path('musician/', views.musician, name="musician")
]
