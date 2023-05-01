from django.shortcuts import render
from .models import AboutUs, Hero, Service, Exercise, Testimonial, FitnessBlog, RecipeItem

def base(request):
    about_us = AboutUs.objects.first()
    hero = Hero.objects.first()
    services = Service.objects.all()
    exercises = Exercise.objects.all()
    testiminials = Testimonial.objects.all()
    fitnessblogs = FitnessBlog.objects.all()
    items = RecipeItem.objects.all()

    context = {
        'about_us': about_us,
        'hero': hero,
        'services': services,
        'exercises': exercises,
        'testimonials': testiminials,
        'fitnessblogs': fitnessblogs,
        'ITEM_TYPE_CHOICES': RecipeItem.ITEM_TYPE_CHOICES,
        'items': items,
        
    
        
  
        
    }
    return render(request, 'base.html', context)

# def blog_detail(request, pk):
#     fitnessblogs = FitnessBlog.objects.all()
#     blog_detail = FitnessBlog.objects.get(id= pk)
#     return render(request, 'blog_detail.html', {
#         'fitnessblogs':fitnessblogs, 
#         'blog_detail':blog_detail,
#         })

def blog_detail(request, pk):
    blog_detail = FitnessBlog.objects.get(id=pk)
    return render(request, 'blog_detail.html', {'blog_detail': blog_detail})



# https://fontawesome.com/icons/dumbbell?f=classic&s=solid