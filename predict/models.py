from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Predict(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    glucose = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    age = models.FloatField()
    result = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"diabetes info of {self.user}"
