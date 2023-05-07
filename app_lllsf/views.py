from django.shortcuts import render
from .models import AboutUs, Hero, Service, Exercise, Testimonial, FitnessBlog, RecipeItem, Category, FitnessBlogComment
from .forms import CommentForm

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

def blog_detail(request, pk):
    blog_detail = FitnessBlog.objects.get(id=pk)
    category = Category.objects.all()
    comments = FitnessBlogComment.objects.filter(parent_comment=None, blog=blog_detail)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog_detail
            comment.save()
            form = CommentForm()
    else:
        form = CommentForm()

    return render(request, 'blog_detail.html', {'blog_detail': blog_detail, 'category': category, 'comments': comments, 'form': form})




def service_detail(request, pk):
    service_detail = Service.objects.get(id=pk)

    return render(request, 'service_detail.html', {'service_detail': service_detail,})


def recipe_detail(request, pk):
    recipe_detail = RecipeItem.objects.get(id=pk)

    return render(request, 'recipe_detail.html', {'recipe_detail': recipe_detail,})
# https://fontawesome.com/icons/dumbbell?f=classic&s=solid


# TODO: contact function, paypal pay, paypal giftcard, get rid of lumia, change colors to dark blue and yellow