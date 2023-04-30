from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    bullet_point_one = models.CharField(max_length=200)
    bullet_point_two = models.CharField(max_length=200)
    image = models.ImageField(upload_to='about_images/')

    def __str__(self):
        return self.title


class IconBox(models.Model):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='icon_boxes')
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Hero(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    button_text = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', default='default_image.jpg')

    def __str__(self):
        return self.title
# In this model, we have defined a Service class with three fields: title, description, and icon_class. title is a character field that will hold the title of the service. description is a text field that will hold the description of the service. icon_class is a character field that will hold the class of the icon to be displayed for the service.
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Exercise(models.Model):
    exercise_type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='exercises/', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    bullet_point_one = models.CharField(max_length=100)
    bullet_point_two = models.CharField(max_length=100)
    percent = models.IntegerField(default=100)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    quote = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class FitnessBlog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title




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
    image = models.ImageField(upload_to='portfolio_images/')
    preview_link = models.URLField()
    details_link = models.URLField()

    def __str__(self):
        return f'{self.name} - {self.item_type}'
    
    



# class RecipeItem(models.Model):
#     name = models.CharField(max_length=200)
#     item_type = models.CharField(max_length=10, choices=[('app', 'App'), ('card', 'Card'), ('web', 'Web')])
#     image = models.ImageField(upload_to='portfolio_images/')
#     preview_link = models.URLField()
#     details_link = models.URLField()