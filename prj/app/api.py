from ninja import NinjaAPI, ModelSchema, Schema
from typing import List
from .models import Game

api = NinjaAPI()

# --- SCHÉMATA ---

class MessageSchema(Schema):
    message: str

class GameOut(ModelSchema):
    class Meta:
        model = Game
        # TADY BYLA CHYBA - musíme explicitně říct, co chceme
        model_fields = "__all__" 

    # Přidáme si hezčí výpis hráčů (nepovinné, ale vypadá to lépe)
    white_player: str = None
    black_player: str = None

    @staticmethod
    def resolve_white_player(obj):
        return f"{obj.white_player.name} {obj.white_player.surname}" if obj.white_player else "Unknown"

    @staticmethod
    def resolve_black_player(obj):
        return f"{obj.black_player.name} {obj.black_player.surname}" if obj.black_player else "Unknown"

class GameCreateIn(Schema):
    """
    Pro vstup (POST/PUT) je bezpečnější použít obyčejné Schema.
    Vyhneš se tak ConfigErroru a lépe se ti budou posílat ID hráčů.
    """
    white_player_id: int
    black_player_id: int
    result: str
    moves: str
    date: str  # Očekává formát YYYY-MM-DD

# --- ENDPOINTY ---

@api.get("/games", response=List[GameOut])
def list_games(request):
    return Game.objects.all()

@api.get("/games/{game_id}", response={200: GameOut, 404: MessageSchema})
def get_game(request, game_id: int):
    try:
        return Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        return 404, {"message": "Game not found"}

@api.post("/games", response={201: GameOut})
def create_game(request, data: GameCreateIn):
    # Rozbalíme data ze schématu přímo do parametrů create()
    game = Game.objects.create(**data.dict())
    return 201, game

@api.put("/games/{game_id}", response={200: GameOut, 404: MessageSchema})
def update_game(request, game_id: int, data: GameCreateIn):
    try:
        game = Game.objects.get(id=game_id)
        for attr, value in data.dict().items():
            setattr(game, attr, value)
        game.save()
        return game
    except Game.DoesNotExist:
        return 404, {"message": "Game not found"}