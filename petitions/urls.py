from django.urls import path
from . import views

urlpatterns = [
    path('', views.petition_list, name='petition_list'),
    path('create/', views.create_petition, name='create_petition'),
    path('vote/<int:petition_id>/', views.vote_petition, name='vote_petition'),
]
