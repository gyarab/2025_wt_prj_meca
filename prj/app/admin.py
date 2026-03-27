from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Player, Game, Tournament, Opening

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'rating', 'birth_year']
    search_fields = ['name', 'surname']
    list_filter = ['birth_year', 'rating']

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ["white_player_link", "black_player_link", "tournament", "opening", "date", "result", "ECO", "moves", "replay_board"]
    list_display_links = ("date",)
    search_fields = [
        "white_player__name", "white_player__surname",
        "black_player__name", "black_player__surname",
        "tournament__name", "opening__name","ECO"
    ]
    list_filter = ["tournament", "opening", "date", "result", "ECO"]
    
    # Přidáme možnost rychle vybrat hráče z dropdownu přímo při editaci
    autocomplete_fields = ["white_player", "black_player", "tournament", "opening"]
    fields = ("white_player", "black_player", "tournament", "opening", "date", "result", "ECO", "moves")
    
    # --- CUSTOM SLOUPCE PRO ODKAZY NA HRÁČE ---
    def white_player_link(self, obj):
        if obj.white_player:
            # Dynamicky získá URL pro úpravu hráče (admin:app_model_change)
            url = reverse(f'admin:{obj._meta.app_label}_player_change', args=[obj.white_player.id])
            return format_html('<a href="{}">{}</a>', url, obj.white_player)
        return "-"
    white_player_link.admin_order_field = "white_player"  # Umožní řadit podle tohoto pole
    white_player_link.short_description = "White Player"  # Nastaví název sloupce v adminu

    def black_player_link(self, obj):
        if obj.black_player:
            # Dynamicky získá URL pro úpravu hráče (admin:app_model_change)
            url = reverse(f'admin:{obj._meta.app_label}_player_change', args=[obj.black_player.id])
            return format_html('<a href="{}">{}</a>', url, obj.black_player)
 
    black_player_link.admin_order_field = "black_player" # Umožní řadit podle tohoto pole
    black_player_link.short_description = "Black Player"  # Nastaví název sloupce v adminu
    
    # --- CUSTOM SLOUPEC PRO PŘEHRÁNÍ PARTIE ---
    def replay_board(self, obj):
        if obj.moves:
            # Vygeneruje tlačítko a uloží do něj tahy (PGN)
            return format_html(
                '<button type="button" class="button replay-btn" data-moves="{}">Přehrát</button>',
                obj.moves
            )
        return "-"
    replay_board.short_description = "Šachovnice"  # Nastaví název sloupce v adminu

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "start_date", "end_date"]
    search_fields = ["name", "location"]
    list_filter = ["start_date", "end_date"]


@admin.register(Opening)
class OpeningAdmin(admin.ModelAdmin):
    list_display = ["name", "moves", "variation", "ECO_code"]
    search_fields = ["name", "ECO_code", "variation"]