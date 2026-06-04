from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.specialization})"
