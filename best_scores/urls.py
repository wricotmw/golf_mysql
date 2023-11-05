
#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('add_golfer/', views.add_golfer, name= "add_golfer"),
    path('add_scores/', views.add_scores, name= "add_scores"),
    path('scores/', views.all_scores, name= "all_scores"),
    path('league/', views.league, name= "league_table"),
]
