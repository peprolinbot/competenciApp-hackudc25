from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Skill, Resource

admin.site.register(User, UserAdmin)
admin.site.register(Skill)
admin.site.register(Resource)
