from ninja import NinjaAPI, ModelSchema, Schema
from typing import List
from .models import Game, Player

api = NinjaAPI()

# --- 1. SCHÉMATA ---

class GameSchema(ModelSchema):
    class Meta:
        model = Game
        exclude = ["white_player", "black_player", "tournament", "opening", "ECO"]
    
    id: int | None      
    white_player: str | None
    black_player: str | None
    tournament: str | None
    opening: str | None  
    date: str | None      # I will leave this as string
    result: str | None
    ECO: str | None
    moves: str | None

class GameListingSchema(Schema):
    count: int
    results: List[GameSchema]

class MessageSchema(Schema):
    message: str

class PlayerSchema(ModelSchema):
    class Meta:
        model = Player
        fields = "__all__"
        
# --- Vstupní schémata (pro POST a PUT) ---
class GameInSchema(Schema):
    white_player_id: int | None = None
    black_player_id: int | None = None
    tournament_id: int | None = None
    opening_id: int | None = None
    date: str | None = None
    result: str | None = None
    ECO: str | None = None 
    moves: str | None = None        
    
# POMOCNÉ FUNKCE
def format_game(game: Game) -> dict:
    white_name = f"{game.white_player.name} {game.white_player.surname}" if game.white_player else "Unknown"
    black_name = f"{game.black_player.name} {game.black_player.surname}" if game.black_player else "Unknown"
    
    return {
        "id": game.id,
        "result": game.result,
        "moves": game.moves,
        "date": str(game.date) if game.date else None,
        "white_player": white_name,
        "black_player": black_name,
        "tournament": game.tournament.name if game.tournament else None,
        "opening": game.opening.name if game.opening else None,
        "ECO": game.ECO if game.ECO else None,
    }    
        
# --- 2. ENDPOINTY ---

@api.get("/games", response=GameListingSchema)
def get_games(request):
    games = Game.objects.select_related("white_player", "black_player", "tournament", "opening").all()
    out = [format_game(game) for game in games]
    return {"count": len(out), "results": out}

@api.get("/games/{game_id}", response={200: GameSchema, 404: MessageSchema})
def get_game(request, game_id: int):
    try:
       game = Game.objects.select_related("white_player", "black_player", "tournament", "opening").get(id=game_id)
       return format_game(game)
    except Game.DoesNotExist:
        return 404, {"message": "Game not found"}
    
# --- SAMOSTUDIUM (POST, PUT) ---

@api.post("/games", response={201: GameSchema})
def create_game(request, payload: GameInSchema):
    # payload.dict() vezme odeslaná JSON data a vytvoří z nich novou partii
    game = Game.objects.create(**payload.dict())
    return 201, format_game(game)

@api.put("/games/{game_id}", response={200: GameSchema, 404: MessageSchema})
def update_game(request, game_id: int, payload: GameInSchema):
    try:
        game = Game.objects.get(id=game_id)
        # Projdeme odeslaná data a upravíme existující partii
        for attr, value in payload.dict().items():
            setattr(game, attr, value)
        game.save()
        return 200, format_game(game)
    except Game.DoesNotExist:
        return 404, {"message": "Game not found"}


# --- DOBROVOLNÉ ROZŠÍŘENÍ (Další business objekt) ---

@api.get("/players", response=List[PlayerSchema])
def get_players(request):
    """Endpoint navíc pro získání extra bodů ze zadání."""
    return Player.objects.all()