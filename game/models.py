from django.db import models

# Create your models here.

class GameClass(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=False, unique=True)
    password = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.username
