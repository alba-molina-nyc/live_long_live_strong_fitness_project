from django.shortcuts import render, redirect
from django.urls import reverse
from .models import AboutUs, Hero, Service, Exercise, Testimonial, FitnessBlog, RecipeItem, Category, FitnessBlogComment, ContactUs
from .forms import CommentForm, ContactUsForm, TestimonialForm

from django.core.mail import send_mail # contactform
from django.conf import settings # contactform
from django.contrib import messages # contactform

def contact_us(request):
    form = ContactUsForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return render(request, 'success.html')
    context = {'form': form}
    return render(request, 'contact_us.html', context)

def about_us(request):
    about_us = AboutUs.objects.first()
    context = {
        'about_us': about_us,
    }
    return render(request, 'about_us.html', context)

def base(request):
    about_us = AboutUs.objects.first()
    hero = Hero.objects.first()
    services = Service.objects.order_by('created_at')[:3]
    exercises = Exercise.objects.all()
    testimonials = Testimonial.objects.all()
    fitnessblogs = FitnessBlog.objects.order_by('created_at')[:3]
    items = RecipeItem.objects.order_by('-created_at')[:3]
    form = ContactUsForm(request.POST or None)


    context = {
        'about_us': about_us,
        'hero': hero,
        'services': services,
        'exercises': exercises,
        'testimonials': testimonials,
        'fitnessblogs': fitnessblogs,
        'ITEM_TYPE_CHOICES': RecipeItem.ITEM_TYPE_CHOICES,
        'items': items,
        'form': form,
    }

    return render(request, 'base.html', context)
   
def blogs(request):
    fitnessblogs = FitnessBlog.objects.all()

    context = {
        'fitnessblogs': fitnessblogs,
    }
    return render(request, 'blogs.html', context)

def blog_detail(request, pk):
    blog_detail = FitnessBlog.objects.get(id=pk)
    category = Category.objects.all()
    comments = FitnessBlogComment.objects.filter(parent_comment=None, blog=blog_detail)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment_body = request.POST.get('comment')
        comment = FitnessBlogComment.objects.create(
            name=name,
            email=email,
            comment_body=comment_body,
            blog=blog_detail
        )
        return redirect(reverse('blog_detail', kwargs={'pk': pk}))

    comment_form = CommentForm()

    return render(request, 'blog_detail.html', {'blog_detail': blog_detail, 'category': category, 'comments': comments, 'comment_form': comment_form})

def services(request):
    services = Service.objects.all()

    context = {
        'services': services,
    }
    return render(request, 'services.html', context)


def service_detail(request, pk):
    service_detail = Service.objects.get(id=pk)

    return render(request, 'service_detail.html', {'service_detail': service_detail,})

def recipes(request):
    items = RecipeItem.objects.all()

    context = {
        'ITEM_TYPE_CHOICES': RecipeItem.ITEM_TYPE_CHOICES,
        'items': items,
    }
    return render(request, 'recipes.html', context)



def recipe_detail(request, pk):
    recipe_detail = RecipeItem.objects.get(id=pk)

    return render(request, 'recipe_detail.html', {'recipe_detail': recipe_detail,})





# https://fontawesome.com/icons/dumbbell?f=classic&s=solid

def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = TestimonialForm()
    return render(request, 'add_testimonial.html', {'form': form})

# TODO:change colors to dark blue and yellow


