from django.contrib import admin
from django.urls import path
from django.urls import include
from WAS import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('course', views.index, name='index'),
    path('admin/', admin.site.urls),
]