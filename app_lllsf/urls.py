from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.about_us, name='about_us'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # # # https://github.com/alba-molina-nyc/tech-talk