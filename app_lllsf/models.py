from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    bullet_point_one = models.CharField(max_length=200)
    bullet_point_two = models.CharField(max_length=200)
    icon_box_one_title = models.CharField(max_length=200)
    icon_box_one_description = models.TextField()
    icon_box_two_title = models.CharField(max_length=200)
    icon_box_two_description = models.TextField()
    image = models.ImageField(upload_to='about_images/')

    def __str__(self):
        return self.title



class Hero(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    button_text = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', default='default_image.jpg')


