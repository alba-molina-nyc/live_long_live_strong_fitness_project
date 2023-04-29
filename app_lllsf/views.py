from django.shortcuts import render
from .models import AboutUs, Hero

def base(request):
    about_us = AboutUs.objects.first()
    hero = Hero.objects.first()
    context = {
        'about_us': about_us,
        'hero': hero,
    }
    return render(request, 'base.html', context)
