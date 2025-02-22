from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.forms.models import model_to_dict
from django.http import JsonResponse

from .models import User, Skill
from .forms import SkillForm, ResourcesForm, SearchSkillForm


from datetime import datetime


def index(request):
    return render(request, 'skill_management/index.html')


@login_required
def new_skill_form(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)

        if form.is_valid():
            if form.is_valid():
                existing_skill = form.cleaned_data.get('existing_skill')
                new_skill = form.cleaned_data.get('new_skill')

            if existing_skill:
                skill = existing_skill
            else:
                skill = Skill.objects.create(name=new_skill)

            skill.owners.add(request.user)
            skill.save()

            messages.success(
                request, "🎉 Skill added succesfully. Now add the resources used to learn this skill.")
            return redirect('skill_management:add_resources_form', skill.id)
    else:
        form = SkillForm()

    return render(request, 'main/show_form.html', {'form_header': 'Select an existing skill or create a new one you learned', 'form': form})


@login_required
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


@login_required
def user_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'skill_management/user_profile.html', {'user': user})


@login_required
@csrf_exempt
def skill_search(request):
    if request.method == 'GET':
        form = SearchSkillForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Skill.objects.filter(
                name__icontains=query)
        else:
            form = SearchSkillForm()
            results = []

    return render(request, 'skill_management/skill_search.html', {'form': form, 'results': results})


@login_required
def skill_info(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    return render(request, 'skill_management/skill_info.html', {'skill': skill})
