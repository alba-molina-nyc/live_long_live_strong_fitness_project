from django.shortcuts import render
from .models import AboutUs, Hero, Service, Exercise, Testimonial, FitnessBlog

def base(request):
    about_us = AboutUs.objects.first()
    hero = Hero.objects.first()
    services = Service.objects.all()
    exercises = Exercise.objects.all()
    testiminials = Testimonial.objects.all()
    fitnessblogs = FitnessBlog.objects.all()
    context = {
        'about_us': about_us,
        'hero': hero,
        'services': services,
        'exercises': exercises,
        'testimonials': testiminials,
        'fitnessblogs': fitnessblogs,
        
    }
    return render(request, 'base.html', context)


# https://fontawesome.com/icons/dumbbell?f=classic&s=solid