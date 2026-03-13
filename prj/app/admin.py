from django.contrib import admin
from .models import Player,Game

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display =['whitePlayer','rating']
    pass

@admin.register(Game)
class GameAdmin(admin.ModelAdmin);
    pass

# Register your models here.
