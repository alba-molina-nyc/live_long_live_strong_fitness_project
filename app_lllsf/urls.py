from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name = "home"),


]

# # # # https://github.com/alba-molina-nyc/tech-talk