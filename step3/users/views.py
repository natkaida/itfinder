from django.shortcuts import render, get_object_or_404
from .models import Profile, Skill

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    main_skills = profile.skills.all()[:2]
    extra_skills = profile.skills.all()[2:]

    context = {'profile': profile, 'main_skills': main_skills,
               "extra_skills": extra_skills}
    return render(request, 'users/user-profile.html', context)

def profiles_by_skill(request, skill_slug):
    skill = get_object_or_404(Skill, slug=skill_slug)
    profiles = Profile.objects.filter(skills__in=[skill])
    context = {
        "profiles": profiles
    }

    return render(request, "users/profiles.html", context)