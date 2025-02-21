from django.forms import ModelForm
from .models import Skill, Resource


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ["name", "description"]


class ResourcesForm(ModelForm):
    class Meta:
        model = Resource
        fields = ["name", "url", "type", "description"]
