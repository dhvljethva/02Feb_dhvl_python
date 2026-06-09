from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True, help_text="Enter a unique username")
    age = models.IntegerField(help_text="Enter user age in years")
    is_public = models.BooleanField(default=True, help_text="Designate if this profile is public or private")

    def __str__(self):
        return self.username
