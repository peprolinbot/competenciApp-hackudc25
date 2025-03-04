# SPDX-FileCopyrightText: 2025 Mario Denis Radu Trifu <m.denis.radu@udc.es>
# SPDX-FileCopyrightText: 2025 Mario Ozón Casais <mario.ozon@udc.es>
# SPDX-FileCopyrightText: 2025 Pedro Rey Anca <personal@peprolinbot.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    role = models.CharField(max_length=128)

    def __str__(self):
        return self.username


class Skill(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    owners = models.ManyToManyField(
        User, related_name='skills', null=True, blank=True)

    def __str__(self):
        return self.name


class Resource(models.Model):
    class ResourceType(models.TextChoices):
        IMAGE = 'Image'
        VIDEO = 'Video'
        WEB = 'Web'
        BOOK = 'Book'
    name = models.CharField(max_length=128)
    url = models.URLField(max_length=256, null=True, blank=True)
    type = models.CharField(max_length=5, choices=ResourceType.choices)
    description = models.TextField()
    skill = models.ForeignKey(
        Skill, on_delete=models.CASCADE, related_name='resources')

    def __str__(self):
        return self.name
