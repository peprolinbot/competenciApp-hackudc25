from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    role = models.CharField(max_length=128)

    def __str__(self):
        return self.username


class Skill(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    owners = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=256, null=True, blank=True)
    type = models.TextChoices("Image", "Video", "Web", "Book")
    description = models.TextField()
    skill = models.ForeignKey(
        Skill, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
