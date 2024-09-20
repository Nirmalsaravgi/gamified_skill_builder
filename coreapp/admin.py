from django.contrib import admin

from players.models import PlayerProfile
from skills.models import Skill, SkillTree
from missions.models import Mission
from rewards.models import Reward
# Register your models here.


admin.site.register(PlayerProfile)
admin.site.register(SkillTree)
admin.site.register(Skill)
admin.site.register(Mission)
admin.site.register(Reward)