from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Exercise(models.Model):
    title = models.CharField(max_length=100)
    reps = models.IntegerField()
    sets = models.IntegerField()
    rest = models.IntegerField()
    completed = models.BooleanField(default=False)