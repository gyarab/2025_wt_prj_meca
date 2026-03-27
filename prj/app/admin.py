from django.contrib import admin
from .models import Player, Game, Tournament, Opening

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'rating', 'birth_year']
    search_fields = ['name', 'surname']
    list_filter = ['birth_year', 'rating']


from django.contrib import admin
from .models import Game, Player, Tournament, Opening

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ["white_player", "black_player", "tournament", "opening", "date", "result"]
    list_display_links = ("white_player", "black_player")
    search_fields = [
        "white_player__name", "white_player__surname",
        "black_player__name", "black_player__surname",
        "tournament__name", "opening__name"
    ]
    list_filter = ["tournament", "opening", "date", "result"]
    
    # Přidáme možnost rychle vybrat hráče z dropdownu přímo při editaci
    autocomplete_fields = ["white_player", "black_player", "tournament", "opening"]
    
    # Pole, která se zobrazí ve formuláři pro úpravu
    fields = ("white_player", "black_player", "tournament", "opening", "date", "result")


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "start_date", "end_date"]
    search_fields = ["name", "location"]
    list_filter = ["start_date", "end_date"]


@admin.register(Opening)
class OpeningAdmin(admin.ModelAdmin):
    list_display = ["name", "moves", "variation", "ECO_code"]
    search_fields = ["name", "ECO_code", "variation"]