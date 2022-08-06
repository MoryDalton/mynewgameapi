from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    loc_x = models.IntegerField()
    loc_w = models.IntegerField()
    loc_d = models.IntegerField()
    user = models.CharField(max_length=255, unique=True)
    win = models.BooleanField(default=False)
    loss = models.BooleanField(default=False)