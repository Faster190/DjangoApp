from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name="main"),
    path("game/<slug:game_slug>/", game_page),
    path("about/", page_about, name="about"),
    path("<slug:game_genre>/", genre_page),
]
