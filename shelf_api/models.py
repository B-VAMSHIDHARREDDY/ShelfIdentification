from django.db import models

# Create your models here.

class ShelfLayout(models.Model):
    layout = models.JSONField()
