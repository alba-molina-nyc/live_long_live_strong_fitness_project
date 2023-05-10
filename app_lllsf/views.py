from django.shortcuts import render, redirect
from django.urls import reverse
from .models import AboutUs, Hero, Service, Exercise, Testimonial, FitnessBlog, RecipeItem, Category, FitnessBlogComment, ContactUs
from .forms import CommentForm, ContactUsForm

from django.core.mail import send_mail # contactform
from django.conf import settings # contactform
from django.contrib import messages # contactform


def base(request):
    about_us = AboutUs.objects.first()
    hero = Hero.objects.first()
    services = Service.objects.all()
    exercises = Exercise.objects.all()
    testimonials = Testimonial.objects.all()
    fitnessblogs = FitnessBlog.objects.all()
    items = RecipeItem.objects.all()

    context = {
        'about_us': about_us,
        'hero': hero,
        'services': services,
        'exercises': exercises,
        'testimonials': testimonials,
        'fitnessblogs': fitnessblogs,
        'ITEM_TYPE_CHOICES': RecipeItem.ITEM_TYPE_CHOICES,
        'items': items,
        'contact_form': ContactUsForm(),
    }
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Your message has been sent. Thank you!')
            # return redirect('base')
        # else:
        #     messages.error(request, 'Error')
    return render(request, 'base.html', context)


# def base(request):
#     about_us = AboutUs.objects.first()
#     hero = Hero.objects.first()
#     services = Service.objects.all()
#     exercises = Exercise.objects.all()
#     testiminials = Testimonial.objects.all()
#     fitnessblogs = FitnessBlog.objects.all()
#     items = RecipeItem.objects.all()

#     context = {
#         'about_us': about_us,
#         'hero': hero,
#         'services': services,
#         'exercises': exercises,
#         'testimonials': testiminials,
#         'fitnessblogs': fitnessblogs,
#         'ITEM_TYPE_CHOICES': RecipeItem.ITEM_TYPE_CHOICES,
#         'items': items,
        
    
        
  
        
#     }
#     return render(request, 'base.html', context)


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         # Save contact information to database
#         contact_us = ContactUs(name=name, email=email, phone=phone, subject=subject, message=message)
#         contact_us.save()
#         print(contact_us.save())

#         messages.success(request, 'Your message has been sent. Thank you!')
#         print('your message has been sent thank you')
#         return redirect('contact')

#     return render(request, 'base.html')




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

def service_detail(request, pk):
    service_detail = Service.objects.get(id=pk)

    return render(request, 'service_detail.html', {'service_detail': service_detail,})


def recipe_detail(request, pk):
    recipe_detail = RecipeItem.objects.get(id=pk)

    return render(request, 'recipe_detail.html', {'recipe_detail': recipe_detail,})
# https://fontawesome.com/icons/dumbbell?f=classic&s=solid


# TODO: contact function, paypal pay, paypal giftcard, get rid of lumia, change colors to dark blue and yellow



# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         # Save contact information to database
#         contact_us = ContactUs(name=name, email=email, phone=phone, subject=subject, message=message)
#         contact_us.save()
#         print(contact_us.save())

#         # Send email
#         # send_mail(
#         #     subject + ' from ' + name,
#         #     message,
#         #     email,
#         #     [settings.DEFAULT_FROM_EMAIL],
#         #     fail_silently=False,
#         # )

#         messages.success(request, 'Your message has been sent. Thank you!')
#         print('your message has been sent thank you')
#         return redirect('contact')

#     return render(request, 'base.html')


