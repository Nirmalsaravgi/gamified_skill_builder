from django.db import models
from coreapp.models import base
# Create your models here.
class Reward(base):
    xp_points = models.IntegerField(default=0, null=True, blank=True)
    skill_points = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.xp_points) or "Unnamed"
    
    # class Meta:
    #     verbose_name_plural = "Rewards"