from django.shortcuts import render
from django.http import HttpResponse
from WAS.models import Course

def index(request):
    category_list = Course.objects.all()
    context_dict = {}
    context_dict['courses'] = category_list
    print(category_list)
    # Render the response and send it back!
    return render(request, 'WAS/index.html', context=context_dict)