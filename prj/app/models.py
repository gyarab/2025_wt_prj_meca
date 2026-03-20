from django.db import models
from django.contrib.auth.models import User
# Create your models here.
   
class Player(models.Model): 
   # id
   name = models.CharField(max_length=255)
   surname = models.CharField(max_length=255)
   rating = models.PositiveSmallIntegerField(blank = True, null = True)
   birth_year = models.PositiveSmallIntegerField(blank = True, null = True)

class Game(models.Model):
   # id
   white_player = models.ForeignKey("Player", related_name="white_games", on_delete= models.SET_NULL, null= True)
   black_player = models.ForeignKey("Player", related_name="black_games", on_delete= models.SET_NULL, null = True)
   tournament = models.ForeignKey("Tournament", on_delete= models.SET_NULL, null = True)
   opening = models.ForeignKey("Opening", on_delete= models.SET_NULL, null = True)
   release_date = models.DateTimeField()
   result = models.CharField(max_length=255)

class Tournament(models.Model):
   # id
   name = models.CharField(max_length=255)
   location = models.CharField(max_length=255)
   start_date = models.DateTimeField()
   end_date = models.DateTimeField()
   
class Opening(models.Model):
   # id
   name = models.CharField(max_length=255)
   moves = models.CharField(max_length=255)  
   variation = models.CharField(max_length=255)
   ECO_code = models.CharField(max_length=255)
     