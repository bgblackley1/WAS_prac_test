from django.urls import path
from WAS import views

app_name = 'WAS'

urlpatterns = [
    path('Course', views.index, name='index'),
]