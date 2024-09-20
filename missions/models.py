from django.db import models
from coreapp.models import base
from skills.models import SkillTree, Skill
from rewards.models import Reward
from tinymce import models as tinymce_models
# Create your models here.
class Mission(base):
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    task = tinymce_models.HTMLField(null=True, blank=True)
    related_skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True, blank=True)
    timelimit = models.TimeField(null=True, blank=True)
    mission_rewards = models.ForeignKey(Reward, null=True, blank=True, on_delete=models.CASCADE)
    mission_status = (
        ('N', 'Not Started'),
        ('Ip', 'In Progress'),
        ('Uc', 'Uncomplete'),
        ('C', 'Completed'),
    )
    status = models.CharField(max_length=256, choices=mission_status)
    completed = models.BooleanField(default=False, null=True, blank=True)
    time_limit = models.DurationField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or "Unnamed"
    
    # class Meta:
    #     verbose_name_plural = "Missions"
