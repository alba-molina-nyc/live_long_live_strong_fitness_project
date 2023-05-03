from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.base, name='base'),
    path('blogs/<int:pk>/', views.blog_detail, name ='blog_detail'),
    path('service/<int:pk>/', views.service_detail, name ='service_detail'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # # # https://github.com/alba-molina-nyc/tech-talk