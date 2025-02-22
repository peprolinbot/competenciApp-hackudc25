from django.forms import ModelForm, Form, CharField
from .models import Skill, Resource


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ["name", "description"]


class ResourcesForm(ModelForm):
    class Meta:
        model = Resource
        fields = ["name", "url", "type", "description"]


class SearchSkillForm(Form):
    query = CharField(label='Search query', max_length=128)
