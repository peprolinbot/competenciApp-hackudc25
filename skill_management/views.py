from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.forms.models import model_to_dict
from django.http import JsonResponse

from .models import User, Skill
from .forms import SkillForm, ResourcesForm, SearchSkillForm


from datetime import datetime


def index(request):
    return render(request, 'skill_management/index.html')


def new_skill_form(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)

        if form.is_valid():
            # TODO: Check if skill already exists
            skill = form.save(commit=False)
            skill.save()

            skill.owners.add(request.user)
            skill.save()

            messages.success(
                request, "🎉 Skill added succesfully. Now add the resources used to learn this skill.")
            return redirect('skill_management:add_resources_form', skill.id)
    else:
        form = SkillForm()

    return render(request, 'main/show_form.html', {'form_header': 'Add the details of the skill you have', 'form': form})


def add_resources_form(request, skill_id):
    if request.method == 'POST':
        form = ResourcesForm(request.POST)

        if form.is_valid():
            resource = form.save(commit=False)
            resource.skill = Skill.objects.get(id=skill_id)
            resource.save()

            messages.success(
                request, "🎉 Skill and resources added succesfully. You can keep adding more resources")
            return redirect('skill_management:add_resources_form', skill_id)
    else:
        form = ResourcesForm()

    return render(request, 'main/show_form.html', {'form_header': 'Add the resources used to learn that skill', 'form': form})


def user_profile(request, user_id):
    user = request.user
    skills = user.skills.all()
    return render(request, 'skill_management/user_profile.html', {'skills': skills})


@csrf_exempt
def skill_search(request):
    form = SearchSkillForm()
    results = []

    if request.method == 'GET':
        form = SearchSkillForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Skill.objects.filter(
                name__icontains=query)

    return render(request, 'skill_management/skill_search.html', {'form': form, 'results': results})


def skill_info(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    return render(request, 'skill_management/skill_info.html', {'skill': skill})
