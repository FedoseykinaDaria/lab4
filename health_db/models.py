from django.db import models

class Note(models.Model):
    name = models.CharField(max_length = 200)
    age = models.IntegerField()
    pressureUP = models.IntegerField()
    pressureDOWN = models.IntegerField()
    cholesterol = models.IntegerField()
    glucose = models.IntegerField()
    sleep_time = models.IntegerField()
    BMI = models.IntegerField()
