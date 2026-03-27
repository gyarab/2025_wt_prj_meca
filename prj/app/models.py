from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField(blank=True, null=True)
    birth_year = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Tournament(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.location})"


class Opening(models.Model):
    name = models.CharField(max_length=255)
    moves = models.CharField(max_length=255)
    variation = models.CharField(max_length=255, blank=True)
    ECO_code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.name} ({self.ECO_code})"


class Game(models.Model):
    RESULT_CHOICES = [
        ("1-0", "1-0"),
        ("0-1", "0-1"),
        ("½-½", "½-½"),
    ]

    white_player = models.ForeignKey(Player, related_name="white_games",
                                     on_delete=models.SET_NULL, null=True)
    black_player = models.ForeignKey(Player, related_name="black_games",
                                     on_delete=models.SET_NULL, null=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.SET_NULL, null=True)
    opening = models.ForeignKey(Opening, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    result = models.CharField(max_length=3, choices=RESULT_CHOICES)
    ECO = models.CharField(max_length=10, blank=True)
    moves = models.TextField(blank=True)

    def __str__(self):
        return f"{self.white_player} vs {self.black_player} ({self.date})"