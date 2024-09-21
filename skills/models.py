from django.db import models
from coreapp.models import base
from players.models import PlayerProfile
from tinymce import models as tinymce_models

# Create your models here.

class SkillTree(base):
    associated_player = models.ForeignKey(PlayerProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, null=True, blank=True)
    level = models.IntegerField(default=0)
    xp_points = models.IntegerField(default=0, null=True, blank=True)
    skill_points = models.IntegerField(default=0, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or "UnTitled"
    
    def add_xp(self, xp):
        """Add XP to the skill tree."""
        self.xp_points += xp

        while self.xp_points >= 1000:
            self.xp_points -= 1000
            self.level += 1

        self.save(update_fields=["xp_points", "level"])

    # def save(self, *args, **kwargs):
    #     while self.xp_points >= 1000:
    #         self.xp_points -= 1000
    #         self.level += 1

class Skill(base):
    name = models.CharField(max_length=256, null=True, blank=True)
    main_goal = tinymce_models.HTMLField(null=True, blank=True)
    description = tinymce_models.HTMLField(null=True, blank=True)
    skill_tree = models.ForeignKey(SkillTree, on_delete=models.CASCADE)
    
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name or "Unnamed"