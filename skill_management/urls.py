from django.urls import path

from . import views

app_name = "skill_management"

urlpatterns = [
    path("", views.index, name="index"),
    path("new_skill", views.new_skill_form, name="new_skill_form"),
    path("skill/<int:skill_id>/add_resources",
         views.add_resources_form, name="add_resources_form")
]
