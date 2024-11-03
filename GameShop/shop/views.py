from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def main_page(request, head="Жанры"):
    head_genre = head
    games = []
    if head == "Жанры":
        games = Games.objects.all().order_by('-id')
    else:
        genre_ = Genre.objects.get(slug=head)
        games = genre_.genre.all()
        head_genre = genre_.name
    result = []
    for game in games:
        list_ = []
        # for gen in game.genre.all():
        #     list_.append(gen)
        # print(list_)
        dict_ = {
            'title': game.title,
            'genre': game.genre.all(),
            'cost': game.cost,
            'photo': game.photo,
            'slug': game.slug
        }
        result.append(dict_)
    context = {
        "games": result,
        'genres': Genre.objects.all(),
        "head": head_genre,
    }
    return render(request, "shop/main.html", context)

def game_page(request, game_slug):
    game = get_object_or_404(Games, slug=game_slug)
    genres = game.genre.all()
    context = {
        "game": game,
        "genre": genres,
        'genres': Genre.objects.all(),
        "head": "Жанры",
    }
    return render(request, "shop/game_page.html", context)

def genre_page(request, game_genre):
    return main_page(request, head=game_genre)


def page_about(request):
    context = {
        'genres': Genre.objects.all(),
        "head": "Жанры",
    }
    return render(request, "shop/about.html", context)
