from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(default="", max_length=100)
    subtitle = models.CharField(default="", max_length=300)
    description = models.TextField(default="")
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
