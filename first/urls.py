from django.urls import path
from . import views
urlpatterns = [
    path("index/",views.index),    
    path("greeting/<str:name>/", views.greeting),
]