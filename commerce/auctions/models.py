from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionList(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1000)
    img = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.id}: Title - {self.title} / Description - {self.description} / Img - {self.img}"
