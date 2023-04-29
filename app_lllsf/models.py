from django.db import models

# class AboutUs(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     bullet_point_one = models.CharField(max_length=200)
#     bullet_point_two = models.CharField(max_length=200)
#     icon_box_one_title = models.CharField(max_length=200)
#     icon_box_one_description = models.TextField()
#     icon_box_two_title = models.CharField(max_length=200)
#     icon_box_two_description = models.TextField()
#     image = models.ImageField(upload_to='about_images/')

#     def __str__(self):
#         return self.title

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

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=50)

# In this model, we have defined a Service class with three fields: title, description, and icon_class. title is a character field that will hold the title of the service. description is a text field that will hold the description of the service. icon_class is a character field that will hold the class of the icon to be displayed for the service.
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=50)