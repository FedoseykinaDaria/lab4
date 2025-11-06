from django.db import models

class Note(models.Model):
    name = models.CharField(max_length = 200)
    age = models.IntegerField(min_value = 1)
    pressureUP = models.IntegerField(min_value = 0)
    pressureDOWN = models.IntegerField(min_value = 0)
    cholesterol = models.IntegerField(min_value = 0)
    glucose = models.IntegerField(min_value = 0)
    sleep_time = models.IntegerField(min_value = 0)
    BMI = models.IntegerField(min_value = 0)
