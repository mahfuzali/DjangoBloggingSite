from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(default="", max_length=100)
    subtitle = models.CharField(default="", max_length=300)
    description = models.TextField(default="")
    date = models.DateField()

    def __str__(self):
        return self.title
