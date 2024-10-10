from django.db import models
class Moviedata(models.Model):
    name=models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    def __str__(self):
        return self.name


# Create your models here.
