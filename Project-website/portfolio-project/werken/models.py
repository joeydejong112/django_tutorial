from django.db import models
from django.contrib.auth.models import User


class Werken(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    url = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/images/')
    icon = models.ImageField(upload_to='media/icon/')
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

