from django.db import models


# Task 1 — UserProfile Model
# This model stores basic profile info: a username, age, and public/private flag.
class UserProfile(models.Model):
    username = models.CharField(max_length=150)       # stores the user's display name
    age = models.IntegerField()                        # stores the user's age (whole number)
    is_public = models.BooleanField(default=True)      # True = profile visible to everyone

    def __str__(self):
        return f"{self.username} (age {self.age})"
