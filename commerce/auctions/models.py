from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    pass

class Auction(models.Model):

    class CategorieOptions(models.IntegerChoices):
        NONE = 1
        SURREALISM = 2
        POP_ART = 3
        MINIMALISM = 4
        STREET_ART = 5

    class StatusOptions(models.IntegerChoices):
        OFF = 0
        ON = 1

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    detail = models.TextField()
    init = models.IntegerField()
    url = models.CharField(max_length=1000, blank=True)
    cat = models.IntegerField(choices=CategorieOptions.choices, default=1)
    status = models.IntegerField(choices=StatusOptions.choices, default=1)

    def __str__(self):
        return f"User: {self.user}, Auct Title: {self.title}, Init value: {self.init}, Cat: {self.cat}"

class Bid(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    toauction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return f"User: {self.user}, Belong (auction) : {self.toauction}, Value: {self.value}"

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    toauction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user}, Belong (auction) : {self.toauction}"

class WatchList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    toauction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    

    
