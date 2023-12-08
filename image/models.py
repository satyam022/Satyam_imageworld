from django.db import models


# Create your models here.


class World(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f"{self.title}"
