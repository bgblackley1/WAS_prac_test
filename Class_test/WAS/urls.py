from django.urls import path
from WAS import views

app_name = 'WAS'

urlpatterns = [
    path('', views.index, name='index'),
    path('course', views.index, name='index'),
]