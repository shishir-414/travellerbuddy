from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio= models.TextField(blank=True, null=True)
    fitness_level = models.IntegerField(default=5) 
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    Experience_Level = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]
    experience=models.CharField(max_length=20, choices=Experience_Level, default="beginner")

    def __str__(self):
        return self.username