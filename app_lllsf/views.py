from django.shortcuts import render
from .models import AboutUs

def about_us(request):
    about_us = AboutUs.objects.first()
    context = {
        'about_us': about_us,
    }
    return render(request, 'base.html', context)
