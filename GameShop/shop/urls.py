from django.urls import path
from .views import *

urlpatterns = [
    # path('about/', about, name="about"),
    path('', main_page, name="main"),
    path("game/<slug:game_slug>/", game_page),
    path("about/", page_about, name="about"),
    path("<slug:game_genre>/", genre_page),
    # path('<int:category>/', main_page_category),
]
