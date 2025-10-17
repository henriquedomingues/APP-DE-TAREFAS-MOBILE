from django.db import models

# Create your models here.

class tblusuarios(models.Model):
    username = models.CharField(max_length=150, null=False)
    password = models.CharField(max_length=128, null=False)
