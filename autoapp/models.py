from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Automobiles(models.Model):
    title = models.CharField(max_length=150)
    short_desc = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title