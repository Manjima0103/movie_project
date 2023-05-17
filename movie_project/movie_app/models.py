from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=250)
    des = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(default="",upload_to='gallery/',)

    def __str__(self):
        return self.name
