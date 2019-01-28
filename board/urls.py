from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("new/", views.new),
    path("create/", views.create),
    path("<int:id>/", views.read),
    
    path("post_new/",views.post_new),
    path("post_create/",views.post_create),
]