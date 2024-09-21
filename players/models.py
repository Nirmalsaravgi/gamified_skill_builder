from django.db import models
from coreapp.models import base
# from tinymce import models as tinymce_models

# Create your models here.
class PlayerProfile(base):
    username = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=500, null=True, blank=True)
    life_goals = models.TextField(null = True, blank = True)
    # avatar = models.FileField(upload_to='avatars/', null=True, blank=True) 
    # badges = 
    # level = models.IntegerField(default=0)
    # Xp_points = models.IntegerField(null=True, blank=True)
    # achivements = 
    player_streak = models.IntegerField(default=0)
    # total_time = 
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username or "Unnamed"