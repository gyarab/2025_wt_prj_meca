from ninja import NinjaAPI, ModelSchema, Schema
from typing import List
from .models import Game

api = NinjaAPI()

class GameSchema(ModelSchema):
    class Meta:
        model = Game
        model_fields = "__all__"
        exclude = [ "white_player", "black_player", "tournament", "opening" ]
        
    white_player: str
    black_player: str
    tournament: str | None
    opening: str | None

class GameListingSchema(Schema):
    count: int
    results: List[GameSchema]
    
@api.get("/games", response=GameListingSchema)
def get_games(request):
    games_qs = Game.objects.select_related("white_player", "black_player", "tournament", "opening").all()
    out = []
    for game in games_qs:
        out.append( {
            "id": game.id,
            "result": game.result,
            "white player": game.white_player.name + " " + game.white_player.surname + " (" + str(game.white_player.rating) + ")",
            "black player": game.black_player.name + " " + game.black_player.surname + " (" + str(game.black_player.rating) + ")",
            "tournament": game.tournament.name if game.tournament else None,
            "opening": game.opening.name if game.opening else None,
            "date": game.date,
        })
    return {
        "count": len(out),
        "results": out
    }
           
@api.get("/games/{game_id}", response=GameSchema)   
def get_game(request, game_id: int):
    try:
        game = Game.objects.select_related("white_player", "black_player", "tournament", "opening").get(id=game_id)           
        return {
            "id:": game.id,
            "result": game.result,
            "white player": game.white_player.name + " " + game.white_player.surname + " (" + str(game.white_player.rating) + ")",
            "black player": game.black_player.name + " " + game.black_player.surname + " (" + str(game.black_player.rating) + ")",
            "tournament": game.tournament.name if game.tournament else None,
            "opening": game.opening.name if game.opening else None,
            "date": game.date, 
            "moves": game.moves,    
        }  
    except Game.DoesNotExist:
        return 404, {"message": "Game not found"}