from django.db import models

# Create your models here.
   
class Player(models.Model): 
   # id
   name = models.CharField(max_length=255)
   surname = models.CharField(max_length=255)
   rating = models.PositiveSmallIntegerField(blank = True, null = True)
   birth_year = models.PositiveSmallIntegerField(blank = True, null = True)

class Game(models.Model):
   # id
   white_player = models.ForeignKey("Player", on_delete= models.SET_NULL, null= True)
   black_player = models.ForeignKey("Player", on_delete= models.SET_NULL, null = True)
   tournament_id = models.ForeignKey("Tournament")
   opening_id = models.ForeignKey("Opening")
   release_date = models.DateTimeField
   result = models.CharField("1-0","1/2-1/2", "0-1")
