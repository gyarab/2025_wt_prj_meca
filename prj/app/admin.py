from django.contrib import admin

from app.models import Player,Game

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display =['name','surname','rating','birth_year']
    pass

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ["white_player","black_player","tournament","opening","release_date","result"]
    pass

# Register your models here.
