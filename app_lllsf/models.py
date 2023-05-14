from django.db import models
from django.utils import timezone
from datetime import datetime

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    bullet_point_one = models.CharField(max_length=200)
    bullet_point_two = models.CharField(max_length=200)
    image = models.ImageField(upload_to='imgs/about_us_images/')

    def __str__(self):
        return f'About Us Section : {self.title} '


class IconBox(models.Model):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='icon_boxes')
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=50)

    def __str__(self):
        return f'About Us Icons : {self.title} '


class Hero(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    button_text = models.CharField(max_length=50)
    image = models.ImageField(upload_to='imgs/hero_images/', default='default_image.jpg')

    def __str__(self):
        return f'Hero Section - {self.title}'
    
# In this model, we have defined a Service class with three fields: title, description, and icon_class. title is a character field that will hold the title of the service. description is a text field that will hold the description of the service. icon_class is a character field that will hold the class of the icon to be displayed for the service.
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=50)
    paragraph_1 = models.TextField(blank=True)
    paragraph_2 = models.TextField(blank=True)
    paragraph_3 = models.TextField(blank=True)
    paragraph_4 = models.TextField(blank=True)
    paragraph_5 = models.TextField(blank=True)
    paragraph_6 = models.TextField(blank=True)
    paragraph_7 = models.TextField(blank=True)
    paragraph_8 = models.TextField(blank=True)
    paragraph_9 = models.TextField(blank=True)
    image = models.ImageField(upload_to='imgs/services/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Exercise(models.Model):
    exercise_type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='imgs/exercises/', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    bullet_point_one = models.CharField(max_length=100)
    bullet_point_two = models.CharField(max_length=100)
    percent = models.IntegerField(default=100)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    age = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='imgs/testimonials/')
    quote = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class FitnessBlog(models.Model):
    CATEGORIES = (
        ('nutrition', 'Nutrition'),
        ('exercise', 'Exercise'),
        ('lifestyle', 'Lifestyle'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='')
    description = models.TextField()
    icon = models.CharField(max_length=50)
    image_1 = models.ImageField(upload_to='imgs/fitnessblogs/', default='default_image.jpg')
    image_2 = models.ImageField(upload_to='imgs/fitnessblogs/', default='default_image.jpg')
    category = models.CharField(max_length=20, choices=CATEGORIES, default='')
    paragraph_1 = models.TextField(blank=True)
    paragraph_2 = models.TextField(blank=True)
    paragraph_3 = models.TextField(blank=True)
    paragraph_4 = models.TextField(blank=True)
    paragraph_5 = models.TextField(blank=True)
    paragraph_6 = models.TextField(blank=True)
    paragraph_7 = models.TextField(blank=True)
    paragraph_8 = models.TextField(blank=True)
    paragraph_9 = models.TextField(blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return self.title



class FitnessBlogComment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_posted = models.DateTimeField(auto_now_add=True)
    comment_body = models.TextField()
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    blog = models.ForeignKey(FitnessBlog, on_delete=models.CASCADE, related_name='comments', default=1)
    icon = models.CharField(max_length=50, default='fa-light fa-user-astronaut')
    def __str__(self):
        return f"{self.name} - {self.date_posted}"

class RecipeItem(models.Model):
    BREAKFAST = 'breakfast'
    LUNCH = 'lunch'
    DINNER = 'dinner'
    SNACK = 'snack'
    ITEM_TYPE_CHOICES = [
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (SNACK, 'Snack'),
    ]
    name = models.CharField(max_length=200)
    item_type = models.CharField(max_length=10, choices=ITEM_TYPE_CHOICES)
    image_finished = models.ImageField(upload_to='imgs/portfolio_images/')
    image_ingredients = models.ImageField(upload_to='imgs/portfolio_images/', default='image_finished')
    image_process = models.ImageField(upload_to='imgs/portfolio_images/', default='image_finished')
    description = models.TextField(blank=True)
    ingredient_1 = models.TextField(blank=True)
    ingredient_2 = models.TextField(blank=True)
    ingredient_3 = models.TextField(blank=True)
    ingredient_4 = models.TextField(blank=True)
    ingredient_5 = models.TextField(blank=True)
    ingredient_6 = models.TextField(blank=True)
    ingredient_7 = models.TextField(blank=True)
    ingredient_8 = models.TextField(blank=True)
    ingredient_9 = models.TextField(blank=True)
    ingredient_10 = models.TextField(blank=True)
    paragraph_1 = models.TextField(blank=True)
    paragraph_2 = models.TextField(blank=True)
    paragraph_3 = models.TextField(blank=True)
    paragraph_4 = models.TextField(blank=True)
    paragraph_5 = models.TextField(blank=True)
    paragraph_6 = models.TextField(blank=True)
    paragraph_7 = models.TextField(blank=True)
    paragraph_8 = models.TextField(blank=True)
    paragraph_9 = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.item_type}'
    

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f'{self.subject} - {self.name}'
