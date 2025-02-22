from django.forms import ModelForm, Form, CharField, ModelChoiceField, ValidationError, Textarea
from .models import Skill, Resource


class SkillForm(Form):
    existing_skill = ModelChoiceField(
        queryset=Skill.objects.all(),
        required=False,
        label="Select Existing Skill"
    )
    new_skill = CharField(
        max_length=128,
        required=False,
        label="New skill name"
    )
    new_skill_description = CharField(
        widget=Textarea,
        max_length=128,
        required=False,
        label="New skill description"
    )

    def clean(self):
        cleaned_data = super().clean()
        existing_skill = cleaned_data.get("existing_skill")
        new_skill = cleaned_data.get("new_skill")

        if not existing_skill and not new_skill:
            raise ValidationError(
                "You must select an existing skill or create a new one.")

        return cleaned_data


class ResourcesForm(ModelForm):
    class Meta:
        model = Resource
        fields = ["name", "url", "type", "description"]


class SearchSkillForm(Form):
    query = CharField(label='Search query', max_length=128)
