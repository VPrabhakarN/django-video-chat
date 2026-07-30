from django.urls import path
from . import views

urlpatterns = [
    path("", views.lobby, name="lobby"),
    path("room/", views.room, name="room"),
    path('get_token/', views.get_token, name="gettoken"),
    path('create_member/', views.create_member, name="createmember"),
    path('get_member/', views.get_member, name="getmember"),
    
]